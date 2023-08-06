# -*- coding: UTF-8 -*-
#   Copyright 2009-2022 Oli Schacher, Fumail Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#
import traceback

from fuglu.shared import ScannerPlugin, DELETE, DUNNO, string_to_actioncode, FileList, get_outgoing_helo, actioncode_to_string
from fuglu.bounce import Bounce
from fuglu.stringencode import force_uString, force_bString
from fuglu.extensions.sql import SQL_EXTENSION_ENABLED, DBFile, DBConfig, RESTAPIError
from fuglu.extensions.redisext import RedisPooledConn, redis, ENABLED as REDIS_ENABLED
from fuglu.extensions.filearchives import Archivehandle
from fuglu.extensions.filetype import filetype_handler
from fuglu.mailattach import NoExtractInfo, Mailattachment
import re
import os
import os.path
import logging
import email
import hashlib
import socket
import json
from threading import Lock
try:
    from domainmagic.rbl import RBLLookup
    DOMAINMAGIC_AVAILABLE = True
except ImportError:
    DOMAINMAGIC_AVAILABLE=False
try:
    import kafka
    KAFKA_AVAILABLE=True
except ImportError:
    KAFKA_AVAILABLE=False


FUATT_NAMESCONFENDING = "-filenames.conf"
FUATT_CTYPESCONFENDING = "-filetypes.conf"
FUATT_ARCHIVENAMESCONFENDING = "-archivenames.conf"
FUATT_ARCHIVENAMES_CRYPTO_CONFENDING = "-archivenames-crypto.conf"
FUATT_ARCHIVECTYPESCONFENDING = "-archivefiletypes.conf"

FUATT_DEFAULT = 'default'

FUATT_ACTION_ALLOW = 'allow'
FUATT_ACTION_DENY = 'deny'
FUATT_ACTION_DELETE = 'delete'

FUATT_CHECKTYPE_FN = 'filename'
FUATT_CHECKTYPE_CT = 'contenttype'

FUATT_CHECKTYPE_ARCHIVE_CRYPTO_FN = 'archive-crypto-filename'
FUATT_CHECKTYPE_ARCHIVE_FN = 'archive-filename'
FUATT_CHECKTYPE_ARCHIVE_CT = 'archive-contenttype'

ATTACHMENT_DUNNO = 0
ATTACHMENT_BLOCK = 1
ATTACHMENT_OK = 2
ATTACHMENT_SILENTDELETE = 3

KEY_NAME = "name"
KEY_CTYPE = "ctype"
KEY_ARCHIVENAME = "archive-name"
KEY_ARCHIVECTYPE = "archive-ctype"
KEY_ENCARCHIVENAME = "enc-archive-name"  # name rules for files in password protected archives


class RulesCache(object):

    """caches rule files"""

    __shared_state = {}

    def __init__(self, rulesdir, nocache: bool = False):
        """Nocache option can be useful for testing"""
        self.__dict__ = self.__shared_state
        if not hasattr(self, 'rules'):
            self.rules = {}
        if not hasattr(self, 'lock'):
            self.lock = Lock()
        if not hasattr(self, 'logger'):
            self.logger = logging.getLogger('fuglu.plugin.FiletypePlugin.RulesCache')
        if not hasattr(self, 'lastreload'):
            self.lastreload = 0
        self.rulesdir = rulesdir
        self._nocache = nocache
        self.reloadifnecessary()

    def getRules(self, ruletype, key):
        self.logger.debug('Rule cache request: [%s] [%s]' % (ruletype, key))
        if ruletype not in self.rules:
            self.logger.error('Invalid rule type requested: %s' % ruletype)
            return None
        if key not in self.rules[ruletype]:
            self.logger.debug('Ruleset not found : [%s] [%s]' % (ruletype, key))
            return None
        self.logger.debug('Ruleset found : [%s] [%s] ' % (ruletype, key))

        ret = self.rules[ruletype][key]
        return ret

    def getCTYPERules(self, key):
        return self.getRules(KEY_CTYPE, key)

    def getARCHIVECTYPERules(self, key):
        return self.getRules(KEY_ARCHIVECTYPE, key)

    def getNAMERules(self, key):
        return self.getRules(KEY_NAME, key)

    def getARCHIVENAMERules(self, key):
        return self.getRules(KEY_ARCHIVENAME, key)

    def getEcryptedARCHIVENAMERules(self, key):
        return self.getRules(KEY_ENCARCHIVENAME, key)

    def reloadifnecessary(self):
        """reload rules if file changed"""
        if not self.rulesdirchanged():
            return
        if not self.lock.acquire():
            return
        try:
            self._loadrules()
        finally:
            self.lock.release()

    def rulesdirchanged(self):
        dirchanged = False
        # if _nocache is True never cache (debugging only)
        if self._nocache:
            return True
        try:
            statinfo = os.stat(self.rulesdir)
        except FileNotFoundError:
            pass
        else:
            ctime = statinfo.st_ctime
            if ctime > self.lastreload:
                dirchanged = True
        return dirchanged

    def _loadrules(self):
        """effectively loads the rules, do not call directly, only through reloadifnecessary"""
        self.logger.debug('Reloading attachment rules...')

        # set last timestamp
        statinfo = os.stat(self.rulesdir)
        ctime = statinfo.st_ctime
        self.lastreload = ctime

        filelist = os.listdir(self.rulesdir)

        newruleset = {KEY_NAME: {}, KEY_CTYPE: {},
                      KEY_ARCHIVENAME: {}, KEY_ARCHIVECTYPE: {},
                      KEY_ENCARCHIVENAME: {}}

        rulecounter = 0
        okfilecounter = 0
        ignoredfilecounter = 0

        for filename in filelist:
            endingok = False
            for ending in FUATT_NAMESCONFENDING, FUATT_CTYPESCONFENDING, FUATT_ARCHIVENAMESCONFENDING, FUATT_ARCHIVECTYPESCONFENDING, FUATT_ARCHIVENAMES_CRYPTO_CONFENDING :
                if filename.endswith(ending):
                    endingok = True
                    break

            if endingok:
                okfilecounter += 1
            else:
                ignoredfilecounter += 1
                self.logger.debug('Ignoring file %s' % filename)
                continue

            ruleset = self._loadonefile("%s/%s" % (self.rulesdir, filename))
            if ruleset is None:
                continue
            rulesloaded = len(ruleset)
            self.logger.debug('%s rules loaded from file %s' %
                              (rulesloaded, filename))
            ruletype = KEY_NAME
            key = filename[0:-len(FUATT_NAMESCONFENDING)]
            if filename.endswith(FUATT_CTYPESCONFENDING):
                ruletype = KEY_CTYPE
                key = filename[0:-len(FUATT_CTYPESCONFENDING)]
            elif filename.endswith(FUATT_ARCHIVENAMESCONFENDING):
                ruletype = KEY_ARCHIVENAME
                key = filename[0:-len(FUATT_ARCHIVENAMESCONFENDING)]
            elif filename.endswith(FUATT_ARCHIVENAMES_CRYPTO_CONFENDING):
                ruletype = KEY_ENCARCHIVENAME
                key = filename[0:-len(FUATT_ARCHIVENAMES_CRYPTO_CONFENDING)]
            elif filename.endswith(FUATT_ARCHIVECTYPESCONFENDING):
                ruletype = KEY_ARCHIVECTYPE
                key = filename[0:-len(FUATT_ARCHIVECTYPESCONFENDING)]

            newruleset[ruletype][key] = ruleset
            self.logger.debug('Updating cache: [%s][%s]' % (ruletype, key))
            rulecounter += rulesloaded

        self.rules = newruleset
        self.logger.info('Loaded %s rules from %s files in %s (%s files ignored)' %
                         (rulecounter, okfilecounter,  self.rulesdir, ignoredfilecounter))

    def _loadonefile(self, filename):
        """returns all rules in a file"""
        if not os.path.exists(filename):
            self.logger.error('Rules File %s does not exist' % filename)
            return None
        if not os.path.isfile(filename):
            self.logger.warning('Ignoring file %s - not a file' % filename)
            return None
        with open(filename) as handle:
            rules = self.get_rules_from_config_lines(handle.readlines())
        return rules

    def get_rules_from_config_lines(self, lineslist):
        ret = []
        for line in lineslist:
            line = line.strip()
            if line.startswith('#') or line == '':
                continue
            tpl = line.split(None, 2)
            if len(tpl) != 3:
                self.logger.debug('Ignoring invalid line  (length %s): %s' % (len(tpl), line))
                continue
            (action, regex, description) = tpl
            action = action.lower()
            if action not in [FUATT_ACTION_ALLOW, FUATT_ACTION_DENY, FUATT_ACTION_DELETE]:
                self.logger.error('Invalid rule action: %s' % action)
                continue

            tp = (action, regex, description)
            ret.append(tp)
        return ret


class FiletypePlugin(ScannerPlugin):

    r"""This plugin checks message attachments. You can configure what filetypes or filenames are allowed to pass through fuglu. If a attachment is not allowed, the message is deleted and the sender receives a bounce error message. The plugin uses the '''file''' library to identify attachments, so even if a smart sender renames his executable to .txt, fuglu will detect it.

Attachment rules can be defined globally, per domain or per user.

Actions: This plugin will delete messages if they contain blocked attachments.

Prerequisites: You must have the python ``file`` or ``magic`` module installed. Additionaly, for scanning filenames within rar archives, fuglu needs the python ``rarfile`` module.


The attachment configuration files are in ``${confdir}/rules``. You should have two default files there: ``default-filenames.conf`` which defines what filenames are allowed and ``default-filetypes.conf`` which defines what content types a attachment may have.

For domain rules, create a new file ``<domainname>-filenames.conf`` / ``<domainname>-filetypes.conf`` , eg. ``fuglu.org-filenames.conf`` / ``fuglu.org-filetypes.conf``

For individual user rules, create a new file ``<useremail>-filenames.conf`` / ``<useremail>-filetypes.conf``, eg. ``oli@fuglu.org-filenames.conf`` / ``oli@fuglu.org-filetypes.conf``

To scan filenames or even file contents within archives (zip, rar), use ``<...>-archivefilenames.conf`` and ``<...>-archivefiletypes.conf``.


The format of those files is as follows: Each line should have three parts, seperated by tabs (or any whitespace):
``<action>``    ``<regular expression>``   ``<description or error message>``

``<action>`` can be one of:
 * allow : this file is ok, don't do further checks (you might use it for safe content types like text). Do not blindly create 'allow' rules. It's safer to make no rule at all, if no other rules hit, the file will be accepted
 * deny : delete this message and send the error message/description back to the sender
 * delete : silently delete the message, no error is sent back, and 'blockaction' is ignored


``<regular expression>`` is a standard python regex. in ``x-filenames.conf`` this will be applied to the attachment name . in ``x-filetypes.conf`` this will be applied to the mime type of the file as well as the file type returned by the ``file`` command.

Example of ``default-filetypes.conf`` :

::

    allow    text        -        
    allow    \bscript    -        
    allow    archive        -            
    allow    postscript    -            
    deny    self-extract    No self-extracting archives
    deny    executable    No programs allowed
    deny    ELF        No programs allowed
    deny    Registry    No Windows Registry files allowed



A small extract from ``default-filenames.conf``:

::

    deny    \.ico$            Windows icon file security vulnerability    
    deny    \.ani$            Windows animated cursor file security vulnerability    
    deny    \.cur$            Windows cursor file security vulnerability    
    deny    \.hlp$            Windows help file security vulnerability

    allow    \.jpg$            -    
    allow    \.gif$            -    



Note: The files will be reloaded automatically after a few seconds (you do not need to kill -HUP / restart fuglu)

Per domain/user overrides can also be fetched from a database instead of files (see dbconnectstring / query options).
The query must return the same rule format as a file would. Multiple columns in the resultset will be concatenated.

The default query assumes the following schema:

::

    CREATE TABLE `attachmentrules` (
      `rule_id` int(11) NOT NULL AUTO_INCREMENT,
      `action` varchar(10) NOT NULL,
      `regex` varchar(255) NOT NULL,
      `description` varchar(255) DEFAULT NULL,
      `scope` varchar(255) DEFAULT NULL,
      `checktype` varchar(20) NOT NULL,
      `prio` int(11) NOT NULL,
      PRIMARY KEY (`rule_id`)
    )

*action*: ``allow``, ``deny``, or ``delete``

*regex*: a regular expression

*description*: description/explanation of this rule which is optionally sent back to the sender if bounces are enabled

*scope*: a domain name or a recipient's email address

*checktype*: one of ``filename``,``contenttype``,``archive-filename``,``archive-contenttype``

*prio*: order in which the rules are run

The bounce template (eg ``${confdir}/templates/blockedfile.tmpl`` ) should
start by defining the headers, followed by a blank line, then the message body for your bounce message. Something like this:

::

    To: ${from_address}
    Subject: Blocked attachment

    Your message to ${to_address} contains a blocked attachment and has not been delivered.

    ${blockinfo}



``${blockinfo}`` will be replaced with the text you specified in the third column of the rule that blocked this message.

The other common template variables are available as well.


"""

    def __init__(self, config, section=None):
        super().__init__(config, section)
        self.requiredvars = {
            'template_blockedfile': {
                'default': '${confdir}/templates/blockedfile.tmpl',
                'description': 'Mail template for the bounce to inform sender about blocked attachment',
            },

            'sendbounce': {
                'default': 'True',
                'description': 'inform the sender about blocked attachments.\nIf a previous plugin tagged the message as spam or infected, no bounce will be sent to prevent backscatter',
            },

            'rulesdir': {
                'default': '${confdir}/rules',
                'description': 'directory that contains attachment rules',
            },

            'blockaction': {
                'default': 'DELETE',
                'description': 'what should the plugin do when a blocked attachment is detected\nREJECT : reject the message (recommended in pre-queue mode)\nDELETE : discard messages\nDUNNO  : mark as blocked but continue anyway (eg. if you have a later quarantine plugin)',
            },

            'dbconnectstring': {
                'default': '',
                'description': 'sqlalchemy connectstring to load rules from a database and use files only as fallback. requires SQL extension to be enabled',
                'confidential': True,
            },

            'query': {
                'default': 'SELECT action,regex,description FROM attachmentrules WHERE scope=:scope AND checktype=:checktype ORDER BY prio',
                'description': "sql query to load rules from a db. #:scope will be replaced by the recipient address first, then by the recipient domain\n:check will be replaced 'filename','contenttype','archive-filename' or 'archive-contenttype'",
            },
            
            'config_section_filename': {
                'default': '',
                'description': 'load additional rules from filter config overrides databases (e.g. from fuglu.conf, yaml, rest api or sql backend)',
            },
    
            'config_section_filetype': {
                'default': '',
                'description': 'load additional rules from filter config overrides databases (e.g. from fuglu.conf, yaml, rest api or sql backend)',
            },
    
            'config_section_archivename': {
                'default': '',
                'description': 'load additional rules from filter config overrides databases (e.g. from fuglu.conf, yaml, rest api or sql backend)',
            },
    
            'config_section_archivecryptoname': {
                'default': '',
                'description': 'load additional rules from filter config overrides databases (e.g. from fuglu.conf, yaml, rest api or sql backend)',
            },
    
            'config_section_archivetype': {
                'default': '',
                'description': 'load additional rules from filter config overrides databases (e.g. from fuglu.conf, yaml, rest api or sql backend)',
            },

            'checkarchivenames': {
                'default': 'False',
                'description': "enable scanning of filenames within archives (zip,rar). This does not actually extract the files, it just looks at the filenames found in the archive."
            },

            'checkarchivecontent': {
                'default': 'False',
                'description': 'extract compressed archives(zip,rar) and check file content type with libmagics\nnote that the files will be extracted into memory - tune archivecontentmaxsize  accordingly.\nfuglu does not extract archives within the archive(recursion)',
            },

            'archivecontentmaxsize': {
                'default': '5000000',
                'description': 'only extract and examine files up to this amount of (uncompressed) bytes',
            },

            'archiveextractlevel': {
                'default': '1',
                'description': 'recursive extraction level for archives. Undefined or negative value means extract until it\'s not an archive anymore'
            },

            'enabledarchivetypes': {
                'default': '',
                'description': 'comma separated list of archive extensions. do only process archives of given types.',
            },

            'problemaction': {
                'default': 'DEFER',
                'description': "action if there is a problem (DUNNO, DEFER)",
            },

        }

        self.logger = self._logger()
        self.rulescache = None
        self.extremeverbosity = False
        self.blockedfiletemplate = ''
        self.sendbounce = True
        self.checkarchivenames = False
        self.checkarchivecontent = False
        self.runtimeconfig = None


        # copy dict with available extensions from Archivehandle
        # (deepcopy is not needed here although in general it is a good idea
        # to use it in case a dict contains another dict)
        #
        # key: file ending, value: archive type
        self.active_archive_extensions = dict(Archivehandle.avail_archive_extensions)


    def examine(self, suspect):
        if self.rulescache is None:
            self.rulescache = RulesCache(self.config.get(self.section, 'rulesdir'))

        self.blockedfiletemplate = self.config.get(self.section, 'template_blockedfile')
        
        try:
            runtimeconfig = DBConfig(self.config, suspect)
            self.checkarchivenames = runtimeconfig.getboolean(self.section, 'checkarchivenames')
            self.checkarchivecontent = runtimeconfig.getboolean(self.section, 'checkarchivecontent')
            self.sendbounce = runtimeconfig.getboolean(self.section, 'sendbounce')
            enabledarchivetypes = runtimeconfig.getlist(self.section, 'enabledarchivetypes')
            if enabledarchivetypes:
                archtypes = list(self.active_archive_extensions.keys())
                for archtype in archtypes:
                    if archtype not in enabledarchivetypes:
                        del self.active_archive_extensions[archtype]
            action, message = self.walk(suspect)
        except RESTAPIError as e:
            action = self._problemcode()
            self.logger.warning(f'{suspect.id} {actioncode_to_string(action)} due to RESTAPIError: {str(e)}')
            message = 'Internal Server Error'
        
        return action, message
    
    
    def asciionly(self, stri):
        """return stri with all non-ascii chars removed"""
        if isinstance(stri, str):
            return stri.encode('ascii', 'ignore').decode()
        elif isinstance(stri, bytes):  # python3
            # A bytes object therefore already ascii, but not a string yet
            return stri.decode('ascii', 'ignore')
        return "".join([x for x in stri if ord(x) < 128])
    
    
    def _tostr(self, stri):
        if isinstance(stri, bytes): # python3 bytes object
            stri = stri.decode('utf-8', 'ignore')
        return stri
    
    
    def matchRules(self, ruleset, obj, suspect, attachmentname=None):
        if attachmentname is None:
            attachmentname = ""
        attachmentname = self.asciionly(attachmentname)

        if obj is None:
            self.logger.warning("%s: message has unknown name or content-type attachment %s" % (suspect.id, attachmentname))
            return ATTACHMENT_DUNNO

        # remove non ascii chars
        asciirep = self.asciionly(obj)

        displayname = attachmentname
        if asciirep == attachmentname:
            displayname = ''

        if ruleset is None:
            return ATTACHMENT_DUNNO

        for action, regex, description in ruleset:
            # database description, displayname and asciirep may be unicode
            description = self._tostr(description)
            displayname = self._tostr(displayname)
            asciirep = self._tostr(asciirep)

            prog = re.compile(regex, re.I)
            if self.extremeverbosity:
                self.logger.debug('%s Attachment %s Rule %s' % (suspect.id, obj, regex))
            if isinstance(obj, bytes):
                obj = obj.decode('UTF-8', 'ignore')
            if prog.search(obj):
                self.logger.debug('%s Rulematch: Attachment=%s Rule=%s Description=%s Action=%s' % (
                    suspect.id, obj, regex, description, action))
                suspect.debug('%s Rulematch: Attachment=%s Rule=%s Description=%s Action=%s' % (
                    suspect.id, obj, regex, description, action))
                if action == 'deny':
                    self.logger.info('%s contains blocked attachment %s %s' % (suspect.id, displayname, asciirep))
                    blockinfo = {f'{displayname} {asciirep}': description}
                    self._blockreport(suspect, blockinfo, enginename='FiletypePlugin')
                    blockinfo = ("%s %s: %s" % (displayname, asciirep, description)).strip()
                    suspect.tags['FiletypePlugin.errormessage'] = blockinfo # deprecated
                    if self.sendbounce:
                        if suspect.is_spam() or suspect.is_virus():
                            self.logger.info(f"{suspect.id} backscatter prevention: not sending attachment block "
                                             f"bounce to {suspect.from_address} - the message is tagged spam or virus")
                        elif not suspect.from_address:
                            self.logger.warning(f"{suspect.id}, not sending attachment block bounce to empty recipient")
                        else:
                            # check if another attachment blocker has already sent a bounce
                            queueid = suspect.get_tag('Attachment.bounce.queueid')
                            if queueid:
                                self.logger.info(f'{suspect.id} already sent attachment block bounce '
                                                 f'to {suspect.from_address} with queueid {queueid}')
                            else:
                                self.logger.debug(f"{suspect.id} sending attachment block "
                                                  f"bounce to {suspect.from_address}")
                                bounce = Bounce(self.config)
                                queueid = bounce.send_template_file(suspect.from_address,
                                                                    self.blockedfiletemplate,
                                                                    suspect,
                                                                    dict(blockinfo=blockinfo))
                                self.logger.info(f'{suspect.id} sent attachment block bounce '
                                                 f'to {suspect.from_address} with queueid {queueid}')
                                suspect.set_tag('Attachment.bounce.queueid', queueid)
                    return ATTACHMENT_BLOCK

                if action == 'delete':
                    self.logger.info('%s contains blocked attachment %s %s -- SILENT DELETE! --' % (suspect.id, displayname, asciirep))
                    return ATTACHMENT_SILENTDELETE

                if action == 'allow':
                    return ATTACHMENT_OK
        return ATTACHMENT_DUNNO
    
    
    def matchMultipleSets(self, setlist, obj, suspect, attachmentname=None):
        """run through multiple sets and return the first action which matches obj"""
        self.logger.debug('%s Checking object %s against attachment rulesets' % (suspect.id, obj))
        for ruleset in setlist:
            res = self.matchRules(ruleset, obj, suspect, attachmentname)
            if res != ATTACHMENT_DUNNO:
                return res
        return ATTACHMENT_DUNNO
    
    
    def _load_rules(self, suspect):
        user_names = []
        user_ctypes = []
        user_archive_names = []
        user_archive_crypto_names = []
        user_archive_ctypes = []
        domain_names = []
        domain_ctypes = []
        domain_archive_names = []
        domain_archive_crypto_names = []
        domain_archive_ctypes = []
        
        for func in [self._load_rules_db, self._load_rules_conf, self._load_rules_file]:
            data = func(suspect)
            if data is None:
                continue
            
            f_user_names, f_user_ctypes, f_user_archive_names, f_user_archive_crypto_names, f_user_archive_ctypes, \
            f_domain_names, f_domain_ctypes, f_domain_archive_names, f_domain_archive_crypto_names, f_domain_archive_ctypes \
                = data
            if f_user_names is not None:
                user_names.extend(f_user_names)
            if f_user_ctypes is not None:
                user_ctypes.extend(f_user_ctypes)
            if f_user_archive_names is not None:
                user_archive_names.extend(f_user_archive_names)
            if f_user_archive_crypto_names is not None:
                user_archive_crypto_names.extend(f_user_archive_crypto_names)
            if f_user_archive_ctypes is not None:
                user_archive_ctypes.extend(f_user_archive_ctypes)
            if f_domain_names is not None:
                domain_names.extend(f_domain_names)
            if f_domain_ctypes is not None:
                domain_ctypes.extend(f_domain_ctypes)
            if f_domain_archive_names is not None:
                domain_archive_names.extend(f_domain_archive_names)
            if f_domain_archive_crypto_names is not None:
                domain_archive_crypto_names.extend(f_domain_archive_crypto_names)
            if f_domain_archive_ctypes is not None:
                domain_archive_ctypes.extend(f_domain_archive_ctypes)
        
        return user_names, user_ctypes, user_archive_names, user_archive_crypto_names, user_archive_ctypes, \
            domain_names, domain_ctypes, domain_archive_names, domain_archive_crypto_names, domain_archive_ctypes
        
        
    def _load_rules_file(self, suspect):
        self.logger.debug('%s Loading attachment rules from filesystem dir %s' % (suspect.id, self.config.get(self.section,'rulesdir')))
        user_names = self.rulescache.getNAMERules(suspect.to_address)
        user_ctypes = self.rulescache.getCTYPERules(suspect.to_address)
        user_archive_names = self.rulescache.getARCHIVENAMERules(suspect.to_address)
        user_archive_crypto_names = self.rulescache.getEcryptedARCHIVENAMERules(suspect.to_address)
        user_archive_ctypes = self.rulescache.getARCHIVECTYPERules(suspect.to_address)

        domain_names = self.rulescache.getNAMERules(suspect.to_domain)
        domain_ctypes = self.rulescache.getCTYPERules(suspect.to_domain)
        domain_archive_names = self.rulescache.getARCHIVENAMERules(suspect.to_domain)
        domain_archive_crypto_names = self.rulescache.getEcryptedARCHIVENAMERules(suspect.to_domain)
        domain_archive_ctypes = self.rulescache.getARCHIVECTYPERules(suspect.to_domain)
        
        return user_names, user_ctypes, user_archive_names, user_archive_crypto_names, user_archive_ctypes, \
               domain_names, domain_ctypes, domain_archive_names, domain_archive_crypto_names, domain_archive_ctypes
    
    
    def _load_rules_db(self, suspect):
        dbconn = ''
        if self.config.has_option(self.section, 'dbconnectstring'):
            dbconn = self.config.get(self.section, 'dbconnectstring')
    
        if dbconn.strip() == '':
            return None
            
        self.logger.debug('%s Loading attachment rules from database' % suspect.id)
        query = self.config.get(self.section, 'query')
        dbfile = DBFile(dbconn, query)
        user_names = self.rulescache.get_rules_from_config_lines(
            dbfile.getContent({'scope': suspect.to_address, 'checktype': FUATT_CHECKTYPE_FN}))
        user_ctypes = self.rulescache.get_rules_from_config_lines(
            dbfile.getContent({'scope': suspect.to_address, 'checktype': FUATT_CHECKTYPE_CT}))
        user_archive_names = self.rulescache.get_rules_from_config_lines(
            dbfile.getContent({'scope': suspect.to_address, 'checktype': FUATT_CHECKTYPE_ARCHIVE_FN}))
        user_archive_crypto_names = self.rulescache.get_rules_from_config_lines(
            dbfile.getContent({'scope': suspect.to_address, 'checktype': FUATT_CHECKTYPE_ARCHIVE_CRYPTO_FN}))
        user_archive_ctypes = self.rulescache.get_rules_from_config_lines(
            dbfile.getContent({'scope': suspect.to_address, 'checktype': FUATT_CHECKTYPE_ARCHIVE_CT}))
        self.logger.debug(
            '%s Found %s filename rules, %s content-type rules, %s archive filename rules, %s archive crypto rules, %s archive content rules for address %s' %
            (suspect.id, len(user_names), len(user_ctypes), len(user_archive_names), len(user_archive_crypto_names), len(user_archive_ctypes),
             suspect.to_address))
    
        domain_names = self.rulescache.get_rules_from_config_lines(
            dbfile.getContent({'scope': suspect.to_domain, 'checktype': FUATT_CHECKTYPE_FN}))
        domain_ctypes = self.rulescache.get_rules_from_config_lines(
            dbfile.getContent({'scope': suspect.to_domain, 'checktype': FUATT_CHECKTYPE_CT}))
        domain_archive_names = self.rulescache.get_rules_from_config_lines(
            dbfile.getContent({'scope': suspect.to_domain, 'checktype': FUATT_CHECKTYPE_ARCHIVE_FN}))
        domain_archive_crypto_names = self.rulescache.get_rules_from_config_lines(
            dbfile.getContent({'scope': suspect.to_domain, 'checktype': FUATT_CHECKTYPE_ARCHIVE_CRYPTO_FN}))
        domain_archive_ctypes = self.rulescache.get_rules_from_config_lines(
            dbfile.getContent({'scope': suspect.to_domain, 'checktype': FUATT_CHECKTYPE_ARCHIVE_CT}))
        self.logger.debug(
            '%s Found %s filename rules, %s content-type rules, %s archive filename rules, %s archive crypto rules, %s archive content rules for domain %s' %
            (suspect.id, len(domain_names), len(domain_ctypes), len(domain_archive_names), len(domain_archive_crypto_names),
             len(domain_archive_ctypes), suspect.to_domain))

        return user_names, user_ctypes, user_archive_names, user_archive_crypto_names, user_archive_ctypes, \
               domain_names, domain_ctypes, domain_archive_names, domain_archive_crypto_names, domain_archive_ctypes
    
    
    def _load_rules_conf(self, suspect):
        user_names = []
        user_ctypes = []
        user_archive_names = []
        user_archive_crypto_names = []
        user_archive_ctypes = []
        domain_names = []
        domain_ctypes = []
        domain_archive_names = []
        domain_archive_crypto_names = []
        domain_archive_ctypes = []
        sections = {
            'config_section_filename': user_names,
            'config_section_filetype': user_ctypes,
            'config_section_archivename': user_archive_names,
            'config_section_archivecryptoname': user_archive_crypto_names,
            'config_section_archivetype': user_archive_ctypes,
        }
        
        if self.runtimeconfig is None or self.runtimeconfig.suspect != suspect:
            self.runtimeconfig = DBConfig(self.config, suspect)
        
        for section in sections:
            self.runtimeconfig.load_section(section)
            options = self.runtimeconfig.get_cached_options(section)
            for regex in options:
                value = self.runtimeconfig.get(section, regex)
                action, description = value.split(None, 1)
                tp = (action, regex, description)
                sections[section].append(tp)
                
        return user_names, user_ctypes, user_archive_names, user_archive_crypto_names, user_archive_ctypes, \
               domain_names, domain_ctypes, domain_archive_names, domain_archive_crypto_names, domain_archive_ctypes


    def walk(self, suspect):
        """walks through a message and checks each attachment according to the rulefile specified in the config"""

        blockaction = self.config.get(self.section, 'blockaction')
        blockactioncode = string_to_actioncode(blockaction)

        user_names, user_ctypes, user_archive_names, user_archive_crypto_names, user_archive_ctypes, \
        domain_names, domain_ctypes, domain_archive_names, domain_archive_crypto_names, domain_archive_ctypes \
            = self._load_rules(suspect)
        
        # always get defaults from file
        default_names = self.rulescache.getNAMERules(FUATT_DEFAULT)
        default_ctypes = self.rulescache.getCTYPERules(FUATT_DEFAULT)
        default_archive_names = self.rulescache.getARCHIVENAMERules(FUATT_DEFAULT)
        default_archive_crypto_names = self.rulescache.getEcryptedARCHIVENAMERules(FUATT_DEFAULT)
        default_archive_ctypes = self.rulescache.getARCHIVECTYPERules(FUATT_DEFAULT)
        
        # get mail attachment objects (only directly attached objects)
        for attObj in suspect.att_mgr.get_objectlist():
            contenttype_mime = attObj.contenttype_mime
            att_name = attObj.filename
            
            if attObj.is_inline or attObj.is_attachment or not attObj.filename_generated:
                # process all attachments marked as "inline", "attachment" or parts
                # with filenames that are not auto-generated
                pass
            else:
                self.logger.debug("%s Skip message object: %s (attachment: %s, inline: %s, auto-name: %s)" % (
                    suspect.id, att_name, attObj.is_attachment, attObj.is_inline, attObj.filename_generated
                ))
                continue
                

            att_name = self.asciionly(att_name)

            res = self.matchMultipleSets([user_names, domain_names, default_names], att_name, suspect, att_name)
            if res == ATTACHMENT_SILENTDELETE:
                self._debuginfo(suspect, "Attachment name=%s SILENT DELETE : blocked by name" % att_name)
                return DELETE, None
            if res == ATTACHMENT_BLOCK:
                self._debuginfo(suspect, "Attachment name=%s : blocked by name)" % att_name)
                message = suspect.tags['FiletypePlugin.errormessage']
                return blockactioncode, message

            # go through content type rules
            res = self.matchMultipleSets([user_ctypes, domain_ctypes, default_ctypes], contenttype_mime, suspect, att_name)
            if res == ATTACHMENT_SILENTDELETE:
                self._debuginfo(suspect, "Attachment name=%s content-type=%s SILENT DELETE: blocked by mime content type (message source)" % (att_name, contenttype_mime))
                return DELETE, None
            if res == ATTACHMENT_BLOCK:
                self._debuginfo(suspect, "Attachment name=%s content-type=%s : blocked by mime content type (message source)" % (att_name, contenttype_mime))
                message = suspect.tags['FiletypePlugin.errormessage']
                return blockactioncode, message

            contenttype_magic = attObj.contenttype
            if contenttype_magic is not None:
                res = self.matchMultipleSets([user_ctypes, domain_ctypes, default_ctypes], contenttype_magic, suspect, att_name)
                if res == ATTACHMENT_SILENTDELETE:
                    self._debuginfo(suspect, "Attachment name=%s content-type=%s SILENT DELETE: blocked by mime content type (magic)" % (att_name, contenttype_magic))
                    return DELETE, None
                if res == ATTACHMENT_BLOCK:
                    self._debuginfo(suspect, "Attachment name=%s content-type=%s : blocked by mime content type (magic)" % (att_name, contenttype_magic))
                    message = suspect.tags['FiletypePlugin.errormessage']
                    return blockactioncode, message

            # archives
            if self.checkarchivenames or self.checkarchivecontent:

                #if archive_type is not None:
                if attObj.is_archive:

                    # check if extension was used to determine archive type and
                    # if yes, check if extension is enabled. This code
                    # is here to remain backward compatible in the behavior. It
                    # is recommended to define inactive archive-types and -extensions
                    # differently
                    if attObj.atype_fromext() is not None:
                        if not attObj.atype_fromext() in self.active_archive_extensions.keys():
                            # skip if extension is not in active list
                            continue


                    self.logger.debug("%s Extracting %s as %s" % (suspect.id, att_name,attObj.archive_type))
                    archivecontentmaxsize = self.config.getint(self.section, 'archivecontentmaxsize')
                    try:
                        archiveextractlevel = self.config.getint(self.section, 'archiveextractlevel')
                        if archiveextractlevel < 0: # value must be greater or equals 0
                            archiveextractlevel = None
                    except Exception:
                        archiveextractlevel = None
                        
                    try:
                        if self.checkarchivenames:
                            # here, check all the filenames, independent of how many files we would extract
                            # by the limits (att_mgr_default_maxnfiles, att_mgr_hard_maxnfiles)
                            if self.checkarchivecontent:
                                namelist = attObj.get_fileslist(0, archiveextractlevel, archivecontentmaxsize, None)
                            else:
                                namelist = attObj.fileslist_archive
                            passwordprotected = attObj.is_protected_archive
                            self.logger.debug(f"{suspect.id} Is {att_name} password protected: {passwordprotected}")
                            ruleset = [user_archive_names, domain_archive_names, default_archive_names]
                            if passwordprotected:
                                ruleset.extend([user_archive_crypto_names, domain_archive_crypto_names, default_archive_crypto_names])

                            for name in namelist:
                                res = self.matchMultipleSets(ruleset, name, suspect, name)
                                if res == ATTACHMENT_SILENTDELETE:
                                    self._debuginfo( suspect, "Blocked filename in archive %s SILENT DELETE" % att_name)
                                    return DELETE, None
                                if res == ATTACHMENT_BLOCK:
                                    self._debuginfo(suspect, "Blocked filename in archive %s" % att_name)
                                    message = suspect.tags['FiletypePlugin.errormessage']
                                    return blockactioncode, message

                        if filetype_handler.available() and self.checkarchivecontent:
                            maxnfiles2extract = suspect.att_mgr.get_maxfilenum_extract(None)
                            nocheckinfo = NoExtractInfo()
                            for archObj in attObj.get_objectlist(0, archiveextractlevel, archivecontentmaxsize, maxnfiles2extract, noextractinfo=nocheckinfo):
                                safename = self.asciionly(archObj.filename)
                                contenttype_magic = archObj.contenttype

                                # Keeping this check for backward compatibility
                                # This could easily be removed since memory is used anyway
                                if archivecontentmaxsize is not None and archObj.filesize > archivecontentmaxsize:
                                    nocheckinfo.append(archObj.filename, "toolarge",
                                                       "already extracted but too large for check: %u > %u"
                                                       % (archObj.filesize, archivecontentmaxsize))
                                    continue

                                res = self.matchMultipleSets(
                                    [user_archive_ctypes, domain_archive_ctypes, default_archive_ctypes],
                                    contenttype_magic, suspect, safename)
                                if res == ATTACHMENT_SILENTDELETE:
                                    self._debuginfo(
                                        suspect, "Extracted file %s from archive %s content-type=%s "
                                                 "SILENT DELETE: blocked by mime content type (magic)"
                                                 % (safename, att_name, contenttype_magic))
                                    return DELETE, None
                                if res == ATTACHMENT_BLOCK:
                                    self._debuginfo(
                                        suspect, "Extracted file %s from archive %s content-type=%s : "
                                                 "blocked by mime content type (magic)"
                                                 % (safename, att_name, contenttype_magic))
                                    message = suspect.tags['FiletypePlugin.errormessage']
                                    return blockactioncode, message

                            for item in nocheckinfo.get_filtered():
                                try:
                                    self._debuginfo(suspect, 'Archive File not checked: reason: %s -> %s' % (item[0], item[1]))
                                except Exception as e:
                                    self._debuginfo(suspect, 'Archive File not checked: %s' % str(e))

                    except Exception as e:
                        self.logger.debug(traceback.format_exc())
                        self.logger.error("%s archive scanning failed in attachment %s: %s" % (suspect.id, att_name, str(e)))
        return DUNNO, None
    
    def walk_all_parts(self, message):
        """Like email.message.Message's .walk() but also tries to find parts in the message's epilogue"""
        for part in message.walk():
            yield part

        boundary = message.get_boundary()
        epilogue = message.epilogue
        if epilogue is None or boundary not in epilogue:
            return

        candidate_parts = epilogue.split(boundary)
        for candidate in candidate_parts:
            try:
                part_content = candidate.strip()
                if part_content.lower().startswith('content'):
                    message = email.message_from_string(part_content)
                    yield message

            except Exception as e:
                self.logger.info("hidden part extraction failed: %s"%str(e))


    def _debuginfo(self, suspect, message):
        """Debug to log and suspect"""
        suspect.debug(message)
        self.logger.debug('%s %s' % (suspect.id, message))
    
    
    def __str__(self):
        return "Attachment Blocker"
    
    
    def lint(self):
        allok = self.check_config() and self.lint_magic() and self.lint_sql() and self.lint_archivetypes()
        return allok
    
    
    def lint_magic(self):
        # the lint routine for magic is now implemented in "filetype.ThreadLocalMagic.lint" and can
        # be called using the global object "filetype_handler"
        return filetype_handler.lint()

    def lint_archivetypes(self):
        if not Archivehandle.avail('rar'):
            print("rarfile library not found, RAR support disabled")
        if not Archivehandle.avail('7z'):
            print("pylzma/py7zlip library not found, 7z support disabled")
        print("Archive scan, available file extensions: %s" % (",".join(sorted(Archivehandle.avail_archive_extensions_list))))
        print("Archive scan, active file extensions:    %s" % (",".join(sorted(self.active_archive_extensions.keys()))))
        return True
    
    
    def lint_sql(self):
        dbconn = ''
        if self.config.has_option(self.section, 'dbconnectstring'):
            dbconn = self.config.get(self.section, 'dbconnectstring')
        if dbconn.strip() != '':
            print("Reading per user/domain attachment rules from database")
            if not SQL_EXTENSION_ENABLED:
                print("Fuglu SQL Extension not available, cannot load attachment rules from database")
                return False
            query = self.config.get(self.section, 'query')
            dbfile = DBFile(dbconn, query)
            try:
                dbfile.getContent(
                    {'scope': 'lint', 'checktype': FUATT_CHECKTYPE_FN})
            except Exception as e:
                import traceback
                print(
                    "Could not get attachment rules from database. Exception: %s" % str(e))
                print(traceback.format_exc())
                return False
        else:
            print("No database configured. Using per user/domain file configuration from %s" %
                  self.config.get(self.section, 'rulesdir'))
        return True



class AttHashAction(ScannerPlugin):
    """
    query attachment hashes against hashbl (e.g. spamhaus or abusix)
    spamhaus: sha256 / b32
    abusix: sha1 / hex
    """
    def __init__(self, config, section=None):
        ScannerPlugin.__init__(self, config, section)
        self.logger = self._logger()
        self.rbllookup = None
        self.requiredvars = {
            'blocklistconfig':{
                'default':'${confdir}/rblatthash.conf',
                'description':'Domainmagic RBL lookup config file',
            },
            'hashalgorithm': {
                'default': 'sha256',
                'description': 'what hash algorithm to use, any supported by hashlib',
            },
            'hashencoding': {
                'default': 'b32',
                'description': 'what hash encoding to use, e.g. hex, b64, b32',
            },
            'enginename': {
                'default': '',
                'description': 'set custom engine name',
            },
            'testhash': {
                'default': 'E5NAEG57WZEJ4VGUOGEZ67NZ2FTD7RUV5QX6FIWEKOFKX5SR7UHQ',
                'description': 'test record in database, used by lint',
            },
        }
        
    
    def _init_rbllookup(self):
        if self.rbllookup is None:
            blocklistconfig = self.config.get(self.section,'blocklistconfig')
            if os.path.exists(blocklistconfig):
                self.rbllookup = RBLLookup()
                self.rbllookup.from_config(blocklistconfig)
                
                
    def _check_hash(self, myhash):
        result = self.rbllookup.listings(myhash)
        return result
    
    
    def lint(self):
        ok = self.check_config()
        if ok and not DOMAINMAGIC_AVAILABLE:
            print('ERROR: domainmagic not available - this plugin will do nothing')
            ok = False
        
        hashenc = self.config.get(self.section, 'hashencoding').lower()
        encoders = [Mailattachment.HASHENC_HEX, Mailattachment.HASHENC_B32, Mailattachment.HASHENC_B64]
        if ok and hashenc not in encoders:
            print(f'ERROR: invalid hashencoding {hashenc}, use one of {", ".join(encoders)}')
            ok = False
        
        hashalgo = self.config.get(self.section, 'hashalgorithm').lower()
        if hashalgo not in hashlib.algorithms_available:
            print(f'ERROR: invalid hash algorithm {hashalgo}, use one of {", ".join(hashlib.algorithms_available)}')
            ok = False
        
        if ok:
            self._init_rbllookup()
            if self.rbllookup is None:
                blocklistconfig = self.config.get(self.section,'blocklistconfig')
                print(f'ERROR: failed to load rbl config from file {blocklistconfig}')
                ok = False
        
        if ok:
            testhash = self.config.get(self.section, 'testhash')
            result = self._check_hash(testhash)
            if not result:
                print(f'ERROR: Hash {testhash} not detected in rbl check')
                ok = False
        
        return ok
    
    
    def examine(self, suspect):
        if not DOMAINMAGIC_AVAILABLE:
            return DUNNO
        self._init_rbllookup()
        if self.rbllookup is None:
            self.logger.error('Not scanning - blocklistconfig could not be loaded')
            return DUNNO
        
        for attobj in suspect.att_mgr.get_objectlist(level=0):
            filename = attobj.filename

            if not attobj.is_attachment:
                self.logger.debug('Skipping inline part with filename: %s' % filename)
                continue
            
            hashalgo = self.config.get(self.section, 'hashalgorithm').lower()
            hashenc = self.config.get(self.section, 'hashencoding').lower()
            myhash = attobj.get_checksum(hashalgo, hashenc, strip=True)
            
            result = self._check_hash(myhash)
            for blockname in result.keys():
                blockinfo = {filename: f'{blockname} {myhash}'}
                enginename = self.config.get(self.section, 'enginename') or None
                self._blockreport(suspect, blockinfo, enginename=enginename)
                self.logger.info('%s attachment hash found: %s in %s' % (suspect.id, myhash, filename))
                break
            if not result:
                self.logger.debug('%s no matching hash found for %s with hash %s' % (suspect.id, filename, myhash))
            
            if suspect.is_blocked():
                break
        else:
            self.logger.debug('%s no attachment to check' % suspect.id)
            
        return DUNNO



class FileHashCheck(ScannerPlugin):
    
    def __init__(self, config, section=None):
        ScannerPlugin.__init__(self, config, section)
        self.redis_pool = None
        self.logger = self._logger()
        
        self.requiredvars = {
            'redis_conn': {
                'default': '',
                'description': 'redis backend database connection: redis://host:port/dbid',
            },
            'pinginterval': {
                'default': '0',
                'description': 'ping redis interval to prevent disconnect (0: don\'t ping)'
            },
            'timeout': {
                'default': '2',
                'description': 'redis/kafka timeout in seconds'
            },
            'hashtype': {
                'default': 'MD5',
                'description': 'the hashing algorithm to be used',
            },
            'extensionsfile': {
                'default': '${confdir}/conf.d/filehash_extensions.txt',
                'description': 'path to file containing accepted file extensions. One per line, comments start after #',
            },
            'hashskiplistfile': {
                'default': '${confdir}/conf.d/filehash_skiphash.txt',
                'description': 'path to file containing skiplisted hashes. One hash per line, comments start after #',
            },
            'filenameskipfile': {
                'default': '${confdir}/conf.d/filehash_skipfilename.txt',
                'description': 'path to file containing file name fragments of file names to be skipped. One per line, comments start after #',
            },
            'allowmissingextension': {
                'default': 'False',
                'description': 'check files without extensions',
            },
            'minfilesize': {
                'default': '100',
                'description': 'minimal size of a file to be checked',
            },
            'minfilesizebyext': {
                'default': 'zip:40',
                'description': 'comma separated list of file type specific min file size overrides. specifiy as ext:size',
            },
            'problemaction': {
                'default': 'DEFER',
                'description': "action if there is a problem (DUNNO, DEFER)",
            },
            
        }
        
        self.minfilesizebyext = None
        self.hashskiplist = None
        self.extensions = None
        self.filenameskip = None
        self.allowmissingextension = False
        self.minfilesize = 100
    
    
    def _to_int(self, value, default=None):
        try:
            value = int(value)
        except ValueError:
            value = default
        return value
    
    
    def _init_databases(self):
        if self.minfilesizebyext is None:
            minfilesizebyext = self.config.getlist(self.section, 'minfilesizebyext')
            self.minfilesizebyext = {}
            for item in minfilesizebyext:
                if not ':' in item:
                    self.logger.error(f'minfilesizebyext {item} is not a valid specification')
                k, v = item.split(':', 1)
                try:
                    v = int(v)
                except ValueError:
                    self.logger.error(f'minfilesizebyext value {v} for {k} is not an integer')
                    continue
                self.minfilesizebyext[k.lower()] = v
        if self.extensions is None:
            filepath = self.config.get(self.section, 'extensionsfile')
            if filepath and os.path.exists(filepath):
                self.extensions = FileList(filename=filepath,
                    lowercase=True, additional_filters=[FileList.inline_comments_filter])
            else:
                self.logger.error(f'extensionfile {filepath} does not exist')
        if self.hashskiplist is None:
            filepath = self.config.get(self.section, 'hashskiplistfile')
            if filepath and os.path.exists(filepath):
                self.hashskiplist = FileList(filename=filepath,
                    lowercase=True, additional_filters=[FileList.inline_comments_filter])
            else:
                self.logger.error(f'hashskiplistfile {filepath} does not exist')
        if self.filenameskip is None:
            filepath = self.config.get(self.section, 'filenameskipfile')
            if filepath and os.path.exists(filepath):
                self.filenameskip = FileList(filename=filepath,
                    lowercase=True, additional_filters=[FileList.inline_comments_filter])
            else:
                self.logger.error(f'filenameskipfile {filepath} does not exist')
        self.allowmissingextension = self.config.getboolean(self.section, 'allowmissingextension')
        self.minfilesize = self.config.getint(self.section, 'minfilesize')
    
    
    def examine(self, suspect):
        if not REDIS_ENABLED:
            return DUNNO
        
        hashtype = self.config.get(self.section, 'hashtype')
        hashtype = hashtype.lower()
        if not hasattr(hashlib, hashtype):
            self.logger.error('invalid hash type %s' % hashtype)
        
        self._init_databases()
        
        if self.hashskiplist:
            hashskiplist = self.hashskiplist.get_list()
        else:
            hashskiplist = []
        
        for attobj in suspect.att_mgr.get_objectlist(level=0):
            filename = attobj.filename
            filecontent = attobj.buffer if attobj.buffer else b""
            
            if not attobj.is_attachment:
                self.logger.debug(f'{suspect.id} Skipping inline part with filename: {filename}')
                continue
            
            if not self._check_filename(filename, len(filecontent)):
                self.logger.debug(f'{suspect.id} Skipping attachment size {len(filecontent)} with filename: {filename}')
                continue
            
            myhash = attobj.get_checksum(hashtype)
            if myhash in hashskiplist:
                self.logger.debug(f'{suspect.id} Skiplisted hash: {myhash}')
                continue
            
            try:
                virusname = self._check_hash(myhash)
                if virusname is not None:
                    blockinfo = {filename: f'{virusname} {myhash}'}
                    self._blockreport(suspect, blockinfo)
                    break
                else:
                    self.logger.debug(f'{suspect.id} no matching hash found for {filename} with hash {myhash}')
            except Exception as e:
                self.logger.error(f'{suspect.id} failed to retrieve hash due to {e.__class__.__name__}: {str(e)}')
                action = self._problemcode()
                message = 'Internal Server Error'
                return action, message
        
        return DUNNO, None
    
    
    def _check_skip(self, suspect):
        skip = None
        if suspect.is_blocked():
            skip = 'blocked'
        elif suspect.is_spam():
            skip = 'spam'
        elif suspect.is_virus():
            skip = 'virus'
        return skip
    
    
    def _lint_redis(self):
        success = True
        redis_conn = self.config.get(self.section, 'redis_conn')
        if redis_conn and not REDIS_ENABLED:
            print('ERROR: redis not available')
            success = False
        elif redis_conn:
            self._init_redis()
            if self.redis_pool is None:
                success = False
                print('ERROR: could not connect to redis server: %s' % redis_conn)
            else:
                try:
                    reply = self.redis_pool.check_connection()
                    if reply:
                        print('OK: redis server replied to ping')
                    else:
                        print('ERROR: redis server did not reply to ping')
                
                except redis.exceptions.ConnectionError as e:
                    success = False
                    print('ERROR: failed to talk to redis server: %s' % str(e))
        else:
            print('INFO: redis disabled')
        return success
    
    
    def lint(self):
        success = self.check_config()
        if not success:
            return success
        
        success = self._lint_redis()
        
        hashtype = self.config.get(self.section, 'hashtype')
        hashtype = hashtype.lower()
        if not hasattr(hashlib, hashtype):
            print('ERROR: invalid hash type %s' % hashtype)
            success = False
        
        self.hashskiplist = FileList(filename=self.config.get(self.section, 'hashskiplistfile'), lowercase=True,
                                     additional_filters=[FileList.inline_comments_filter])
        if self.hashskiplist.get_list():
            print('WARNING: empty hash skiplist')
        
        self.extensions = FileList(filename=self.config.get(self.section, 'extensionsfile'), lowercase=True,
                                   additional_filters=[FileList.inline_comments_filter])
        ext = self.extensions.get_list()
        if len(ext) == 0:
            success = False
            print('WARNING: extensions list is empty')
        else:
            print('INFO: checking %s extensions' % len(ext))
        
        self.filenameskip = FileList(filename=self.config.get(self.section, 'filenameskipfile'),
                                     lowercase=True, additional_filters=[FileList.inline_comments_filter])
        if len(self.filenameskip.get_list()) == 0:
            success = False
            print('WARNING: extensions list is empty')
        
        return success
    
    
    def _init_redis(self):
        """
        initializes Redis on first call and returns the Redis connection object. Aborts the program if redis configuration is malformed.
        :return: (RedisKeepAlive)
        """
        if self.redis_pool is None:
            redis_conn = self.config.get(self.section, 'redis_conn')
            if redis_conn:
                timeout = self.config.getint(self.section, 'timeout'),
                pinginterval = self.config.getint(self.section, 'pinginterval')
                self.redis_pool = RedisPooledConn(redis_conn, socket_keepalive=True, socket_timeout=timeout, pinginterval=pinginterval)
    
    
    def _check_hash(self, myhash):
        virusname = None
        self._init_redis()
        
        if self.redis_pool is not None:
            attempts = 2
            while attempts:
                attempts -= 1
                try:
                    self.redis_pool: RedisPooledConn
                    redisconn = self.redis_pool.get_conn()
                    result = redisconn.hmget(myhash, ['virusname'])
                    if result:
                        virusname = force_uString(result[0])
                    attempts = 0
                except redis.exceptions.ConnectionError as e:
                    msg = f"problem in {self.__class__.__name__} getting virusname for hash {myhash}"
                    self.logger.warning(msg) if attempts else self.logger.error(msg, exc_info=e)
                except (socket.timeout, redis.exceptions.TimeoutError):
                    self.logger.info("Socket timeout in check_hash")
        return virusname
    
    
    def _check_filename(self, filename, filesize, force=False, ignore_upn=False, ignore_dotfiles=False):
        ok = True
        
        if ignore_upn:
            for i in filename:
                if ord(i) > 128:
                    self.logger.debug('skipping file %s - name contains upn' % filename)
                    ok = False
                    break
        
        if ok and filename in ['unnamed.htm', 'unnamed.txt']:  # ignore text and html parts of mail
            ok = False
        
        if ok and ignore_dotfiles and filename.startswith('.'):
            self.logger.debug('skipping file %s - is hidden' % filename)
            ok = False
        
        lowerfile = filename.lower()
        try:
            ext = lowerfile.rsplit('.', 1)[1]
        except IndexError:
            ext = ''
        
        if ok and self.extensions and ext != '':
            if ext not in self.extensions.get_list() and not force:
                self.logger.debug('skipping file %s - extension not in my list' % filename)
                ok = False
        elif ok:
            if not self.allowmissingextension and not force:
                self.logger.debug('skipping file %s with missing extension' % filename)
                ok = False
        
        if ok and self.filenameskip and not force:
            for badword in self.filenameskip.get_list():
                if badword in lowerfile:
                    self.logger.debug("filename %s contains bad word '%s' - skipping" % (filename, badword))
                    ok = False
                    break
            
            if ok and ext in self.minfilesizebyext:
                if filesize < self.minfilesizebyext[ext]:
                    self.logger.debug('%s too small for extension %s (%s bytes)' % (filename, ext, filesize))
                    ok = False
            elif ok and filesize < self.minfilesize:
                self.logger.debug('ignoring small file %s (%s bytes)' % (filename, filesize))
                ok = False
        
        return ok


class FileHashRedis(object):
    def __init__(self, redis_pool, ttl, logger):
        self.redis_pool = redis_pool
        self.ttl = ttl
        self.logger = logger
    
    def insert(self, myhash, messagebytes, age=0):
        values = json.loads(messagebytes)
        filename = values.get('filename')
        virusname = values.get('virusname')
        filesize = values.get('filesize')
        
        td = int(self.ttl-age)
        if td <= 0:
            self.logger.debug(f'skipping old hash {myhash} with age {age}')
            return
        
        try:
            redisconn = self.redis_pool.get_conn()
            result = redisconn.hmget(myhash, ['virusname', 'filesize'])
            pipe = redisconn.pipeline()
            if result and result[1] == filesize:
                virusname = result[0]
                self.logger.debug('known hash %s has virus name %s' % (myhash, virusname))
            else:
                redisconn.hset(myhash, mapping=dict(filename=filename, filesize=filesize, virusname=virusname))
            pipe.expire(myhash, td)
            pipe.execute()
        except redis.exceptions.ConnectionError as e:
            self.logger.warning(f'failed to insert hash in redis due to {e.__class__.__name__}: {str(e)}')
        except (socket.timeout, redis.exceptions.TimeoutError):
            self.logger.info("Socket timeout in insert_redis")


class FileHashFeeder(FileHashCheck):
    def __init__(self,config,section=None):
        FileHashCheck.__init__(self,config,section)
        self.logger = self._logger()
        
        requiredvars = {
            'prefix': {
                'default': 'FH.GEN',
                'description': 'virus name prefix',
            },
            'expirationdays': {
                'default':'3',
                'description':'days until hash expires',
            },
            'kafkahosts': {
                'default': '',
                'description:': 'kafka bootstrap hosts: host1:port host2:port'
            },
            'kafkatopic': {
                'default': 'filehash',
                'description': 'name of kafka topic'
            },
            'kafkausername': {
                'default': '',
                'description:': 'kafka sasl user name for this producer'
            },
            'kafkapassword': {
                'default': '',
                'description': 'kafka sals password for this producer'
            },
        }
        self.requiredvars.update(requiredvars)
        
        self.kafkaproducer = None
        self.kafkatopic = None
        self.delta_expiration = 0


    def lint(self):
        success = FileHashCheck.lint(self)
        expirationdays = self.config.get(self.section, 'expirationdays')
        try:
            int(expirationdays)
        except ValueError:
            success = False
            print('ERROR: expirationdays must be a number. current value: %s' % expirationdays)
        if self.config.get(self.section, 'kafkahosts'):
            try:
                self._init_kafka()
            except kafka.errors.KafkaError as e:
                print('ERROR: failed to connect to kafka: %s' % str(e))
                success = False
            except Exception as e:
                print('ERROR: Error connecting to kafka: %s' % str(e))
                self.logger.exception(e)
                success = False
        else:
            print('INFO: kafka disabled')
        return success

    def process(self, suspect, decision):
        self._run(suspect)
    
    
    def examine(self, suspect):
        self._run(suspect)
        return DUNNO, None
    
    
    def _run(self, suspect):
        hashtype = self.config.get(self.section, 'hashtype')
        hashtype = hashtype.lower()
        if not hasattr(hashlib, hashtype):
            self.logger.error('invalid hash type %s' % hashtype)

        self._init_databases()
        self.delta_expiration = self.config.getint(self.section, 'expirationdays') * 86400
        
        if self.hashskiplist:
            hashskiplist = self.hashskiplist.get_list()
        else:
            hashskiplist = []
        
        for attobj in suspect.att_mgr.get_objectlist(level=0):
            filename = attobj.filename
            filecontent = attobj.buffer if attobj.buffer else b""
            if not self._check_filename(filename, len(filecontent)):
                continue

            myhash = attobj.get_checksum(hashtype)
            if myhash in hashskiplist:
                self.logger.debug('Skiplisted hash: %s' % myhash)
                continue
            
            virusname = attobj.get_mangled_filename(prefix=self.config.get(self.section, 'prefix'))
            messagebytes = json.dumps({'filename':filename, 'virusname':virusname, 'filesize':len(filecontent), 'filehash':myhash}).encode()
            if self.config.get(self.section, 'redis_conn'):
                self._insert_redis(myhash, messagebytes)
            if self.config.get(self.section, 'kafkahosts'):
                try:
                    self._insert_kafka(myhash, messagebytes)
                    self.logger.info('%s logged hash %s to kafka' % (suspect.id, myhash))
                except kafka.errors.KafkaError as e:
                    self.logger.error('%s failed to log hash %s due to %s' % (suspect.id, myhash, str(e)))
    
    
    def _insert_redis(self, myhash, messagebytes):
        self._init_redis()
        redisbackend = FileHashRedis(self.redis_pool, self.delta_expiration, self.logger)
        redisbackend.insert(myhash, messagebytes, 0)
    
    
    def _init_kafka(self):
        if self.kafkaproducer is not None:
            return
        self.bootstrap_servers = self.config.getlist(self.section, 'kafkahosts')
        if self.bootstrap_servers:
            self.kafkatopic = self.config.get(self.section, 'kafkatopic')
            timeout = self.config.getint(self.section, 'timeout')
            username = self.config.get(self.section, 'kafkausername')
            password = self.config.get(self.section, 'kafkapassword')
            clientid = 'prod-fuglu-%s-%s' % (self.__class__.__name__, get_outgoing_helo(self.config))
            self.kafkaproducer = kafka.KafkaProducer(bootstrap_servers=self.bootstrap_servers, api_version=(0, 10, 1), client_id=clientid,
                                                     request_timeout_ms=timeout*1000, sasl_plain_username=username, sasl_plain_password=password)
    
    
    def _insert_kafka(self, myhash, messagebytes):
        if self.kafkaproducer is None:
            self._init_kafka()
        try:
            self.kafkaproducer.send(self.kafkatopic, value=messagebytes, key=force_bString(myhash))
        except Exception as e:
            self.kafkaproducer = None
            raise e

