import re
from os import environ
from Script import script 
from time import time


id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
USER_SESSION = environ.get('USER_SESSION', 'User_Bot')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']
USERBOT_STRING_SESSION = environ.get('USERBOT_STRING_SESSION')

#Clone
#CLONE_SESSIONS = {}
#CLONED_SESSIONS = []

# FSUB
auth_channel = environ.get('AUTH_CHANNEL')
AUTH_CHANNEL = int(environ.get("AUTH_CHANNEL", "-1001943335054"))
# Set to False inside the bracket if you don't want to use Request Channel else set it to Channel ID
REQ_CHANNEL = environ.get("REQ_CHANNEL", "False")
REQ_CHANNEL = int(REQ_CHANNEL) if REQ_CHANNEL and id_pattern.search(REQ_CHANNEL) else False
JOIN_REQS_DB = environ.get("JOIN_REQS_DB", 'DATABASE_URI')
group_sub = environ.get('GROUP_SUB')

#rename
FLOOD = int(environ.get("FLOOD", "10"))
RENAME_MODE = bool(environ.get("RENAME_MODE"))

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

PICS = (environ.get('PICS', 'https://telegra.ph/file/5083526feada50efd29dc.jpg https://telegra.ph/file/a014d59bbc4a3917158d3.jpg https://telegra.ph/file/0ce3fdbe4369cad5e0113.jpg https://telegra.ph/file/7c0f6910bd34093983bd9.jpg https://telegra.ph/file/b4553c00050dec17487e9.jpg https://telegra.ph/file/720fb80700e0a6451f79a.jpg https://telegra.ph/file/4c25bfea6ed967ea9f10f.jpg https://telegra.ph/file/f4869c934a7f2eaa31f79.jpg https://telegra.ph/file/9f6bfb939571221e1763b.jpg https://telegra.ph/file/62d8cd682baba8d85b802.jpg')).split()
NOR_IMG = environ.get("NOR_IMG", "https://telegra.ph/file/b856bcc3281a959e80b0e.jpg")
NEWGRP = environ.get("NEWGRP", "https://telegra.ph/file/761b1bf4494bb986507ce.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://telegra.ph/file/91bd6cd35cb853bef9baa.mp4")
SPELL_IMG = environ.get("SPELL_IMG", "")
SP = (environ.get('SP', '')).split()


#Auto approve 
CHAT_ID = [int(app_chat_id) if id_pattern.search(app_chat_id) else app_chat_id for app_chat_id in environ.get('CHAT_ID', '-1001908151821').split()]
TEXT = environ.get("APPROVED_WELCOME_TEXT", "<b>Dᴇᴀʀ {mention}\n\nYour Request To Jᴏɪɴ {title}  Was Approved 🔆</b>")
APPROVED = environ.get("APPROVED_WELCOME", "on").lower()

#Ai
AI = is_enabled((environ.get("AI","True")), True)
OPENAI_API = environ.get("OPENAI_API","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")
AI_LOGS = int(environ.get("AI_LOGS","-1001774912790")) #GIVE YOUR NEW LOG CHANNEL ID TO STORE MESSAGES THAT THEY SEARCH IN BOT PM.... [ i have added this to keep an eye on the users message, to avoid misuse of LazyPrincess ]


# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6327489457 2034319320').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001979254627 -1001530438262 -1001979254627 -1001891660326 -1001973908906 -1001908151821').split()] # alpha dump channel id -1001973908906

LANGUAGES = ["malayalam", "tamil", "english", "hindi", "telugu", "kannada"]


auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '6327489457').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID')
reqst_channel = environ.get('REQST_CHANNEL_ID','-1001908151821')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
support_chat_id = environ.get('SUPPORT_CHAT_ID','-1001975148351')
login_channel = environ.get('LOGIN_CHANNEL')
LOGIN_CHANNEL = environ.get('LOGIN_CHANNEL', "-1001943335054")
PM_TEXTS = int(environ.get('PM_TEXTS', '-1001846311583'))


# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://sri:sri@cluster0.twm8vnp.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# MongoDB information of (user)
USER_DATABASE_URI = environ.get('USER_DATABASE_URI', "mongodb+srv://userdb:userdb@cluster0.e2lx0zg.mongodb.net/?retryWrites=true&w=majority")
USER_DATABASE_NAME = environ.get('USER_DATABASE_NAME', "cluster0")

# Custom Chats
FILE_CHANNEL = int(environ.get('FILE_CHANNEL', '-1001966097254'))
FILE_CHANNEL_LINK = environ.get('FILE_CHANNEL_LINK', 'https://t.me/Bullet_Data')

# This is required for the plugins involving the file system.
TMP_DOWNLOAD_DIRECTORY = environ.get("TMP_DOWNLOAD_DIRECTORY", "./DOWNLOADS/")

# Command
COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "/")

#Downloader
DOWNLOAD_LOCATION = environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/AudioBoT/")


SHORTLINK_URL = environ.get('SHORTLINK_URL', '')
SHORTLINK_API = environ.get('SHORTLINK_API', '')

#group and channel links
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/+k-0-OWAtrkoyM2Y1')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/+DIFevVBulGYzYzk1')
M_GRP_LINK = environ.get('M_GRP_LINK', 'https://t.me/+cft-rB6cc_o4OWFl')

# Others
VERIFY = bool(environ.get('VERIFY', False))
# SHORTLINK_URL = environ.get('SHORTLINK_URL', 'http://TinyFy.in')
# SHORTLINK_API = environ.get('SHORTLINK_API', '5f301bd41650cf7f64b9e7434fef3b7c973918df')
IS_SHORTLINK = bool(environ.get('IS_SHORTLINK', False))
NO_RESULTS_MSG = bool(environ.get('NO_RESULTS_MSG', False))
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
MAX_B_TN = environ.get("MAX_B_TN", "7")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "False")), False)
PORT = environ.get("PORT", "8080")
MSG_ALRT = environ.get('MSG_ALRT', 'Piracy Is Crime')
NOR_ALRT =  environ.get('NOR_ALRT', 'NO IMAGES IS FOUND')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001924870738'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'Nothing_Support_Group')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "False")), False)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CUSTOM_FILE_CAPTION}")
CUSTOM_QUERY_CAPTION = environ.get("CUSTOM_QUERY_CAPTION", f"{script.CUSTOM_QUERY_CAPTION}")
CAPTION = environ.get("CAPTION", f"{script.CAPTION}")
BR_IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.BR_TEMPLATE_TXT}")
BATCH_LINK = environ.get('BATCH_LINK',"")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", f"{script.CUSTOM_FILE_CAPTION}")
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

#redict
MAIN_CHANNEL = environ.get('MAIN_CHANNEL',"https://t.me/+DIFevVBulGYzYzk1")
FILE_FORWARD = environ.get('FILE_FORWARD',"https://t.me/+hHHW8TOqFhE1OWQ1")
MSG_ALRT = environ.get('MSG_ALRT', '𝑪𝑯𝑬𝑪𝑲 & 𝑻𝑹𝒀 𝑨𝑳𝑳 𝑴𝒀 𝑭𝑬𝑨𝑻𝑼𝑹𝑬𝑺')
FILE_CHANNEL = int(environ.get('FILE_CHANNEL', 0))

#LANGUAGES = ["MALAYALAM", "TAMIL", "ENGLISH", "HINDI", "TELUGU", "KANNADA" "DUBBED"]

# Delete Time
IMDB_DLT_TIME = int(environ.get('IMDB_DLT_TIME', 600))
DLT_TIME = int(environ.get('DLT_TIME', 20))

# heroku
HRK_APP_NAME = environ.get('HRK_APP_NAME', 'mybots')
HRK_API = environ.get('HRK_API', '0')



LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
