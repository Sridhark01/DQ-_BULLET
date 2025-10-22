import re
from os import environ
from Script import script
from time import time


# ────────────────────────── Helper Functions ────────────────────────── #

id_pattern = re.compile(r'^.\d+$')

def is_enabled(value, default):
    """Convert string booleans like 'true', 'yes', etc. to Python bools."""
    if str(value).lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif str(value).lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


# ────────────────────────── Bot Information ────────────────────────── #

SESSION = environ.get('SESSION', 'Media_search')
USER_SESSION = environ.get('USER_SESSION', 'User_Bot')

# ✅ Fixed tuple bug — correct use of environ.get()
API_ID = int(environ.get("API_ID", "13859375"))
API_HASH = environ.get("API_HASH", "6ae4ba5fdc4eb0948616585a5bb7ee58")
BOT_TOKEN = environ.get("BOT_TOKEN", "6372243428:AAH0_ZcT7t-MiSuQnIiVSNit6TBZegYw3CE")

USERBOT_STRING_SESSION = environ.get('USERBOT_STRING_SESSION')

# ────────────────────────── Channels & Authorization ────────────────────────── #

AUTH_CHANNEL = int(environ.get("AUTH_CHANNEL", "-1001943335054"))
REQ_CHANNEL = environ.get("REQ_CHANNEL", "False")
REQ_CHANNEL = int(REQ_CHANNEL) if REQ_CHANNEL and id_pattern.search(REQ_CHANNEL) else False
LOGIN_CHANNEL = int(environ.get("LOGIN_CHANNEL", "-1001943335054"))
JOIN_REQS_DB = environ.get("JOIN_REQS_DB", 'DATABASE_URI')
GROUP_SUB = environ.get('GROUP_SUB')

# ────────────────────────── Bot Settings ────────────────────────── #

FLOOD = int(environ.get("FLOOD", "10"))
RENAME_MODE = bool(environ.get("RENAME_MODE"))

CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = is_enabled(environ.get('USE_CAPTION_FILTER', "True"), True)

# Bot media
PICS = (environ.get('PICS', 
    'https://telegra.ph/file/5083526feada50efd29dc.jpg '
    'https://telegra.ph/file/a014d59bbc4a3917158d3.jpg '
    'https://telegra.ph/file/0ce3fdbe4369cad5e0113.jpg '
    'https://telegra.ph/file/7c0f6910bd34093983bd9.jpg '
    'https://telegra.ph/file/b4553c00050dec17487e9.jpg '
    'https://telegra.ph/file/720fb80700e0a6451f79a.jpg '
    'https://telegra.ph/file/4c25bfea6ed967ea9f10f.jpg '
    'https://telegra.ph/file/f4869c934a7f2eaa31f79.jpg '
    'https://telegra.ph/file/9f6bfb939571221e1763b.jpg '
    'https://telegra.ph/file/62d8cd682baba8d85b802.jpg')).split()

NOR_IMG = environ.get("NOR_IMG", "https://telegra.ph/file/b856bcc3281a959e80b0e.jpg")
NEWGRP = environ.get("NEWGRP", "https://telegra.ph/file/761b1bf4494bb986507ce.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://telegra.ph/file/91bd6cd35cb853bef9baa.mp4")
SPELL_IMG = environ.get("SPELL_IMG", "")
SP = (environ.get('SP', '')).split()

# ────────────────────────── Auto-Approve ────────────────────────── #

CHAT_ID = [int(cid) if id_pattern.search(cid) else cid for cid in environ.get('CHAT_ID', '-1001908151821').split()]
TEXT = environ.get("APPROVED_WELCOME_TEXT", "<b>Dᴇᴀʀ {mention}\n\nYour Request To Jᴏɪɴ {title} Was Approved 🔆</b>")
APPROVED = environ.get("APPROVED_WELCOME", "on").lower()

# ────────────────────────── AI & OpenAI ────────────────────────── #

AI = is_enabled(environ.get("AI", "True"), True)
OPENAI_API = environ.get("OPENAI_API", "sk-xxxxx")
AI_LOGS = int(environ.get("AI_LOGS", "-1001774912790"))

# ────────────────────────── Admins & Channels ────────────────────────── #

ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6327489457 2034319320').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001979254627 -1001530438262 -1001891660326').split()]

LANGUAGES = ["malayalam", "tamil", "english", "hindi", "telugu", "kannada"]

AUTH_USERS = [int(u) if id_pattern.search(u) else u for u in environ.get('AUTH_USERS', '6327489457').split()] + ADMINS
SUPPORT_CHAT_ID = int(environ.get('SUPPORT_CHAT_ID', '-1001975148351'))

# ────────────────────────── MongoDB Config ────────────────────────── #

DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://sri:sri@cluster0.twm8vnp.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

USER_DATABASE_URI = environ.get('USER_DATABASE_URI', "mongodb+srv://userdb:userdb@cluster0.e2lx0zg.mongodb.net/?retryWrites=true&w=majority")
USER_DATABASE_NAME = environ.get('USER_DATABASE_NAME', "cluster0")

# ────────────────────────── File & Directory Config ────────────────────────── #

FILE_CHANNEL = int(environ.get('FILE_CHANNEL', '-1001966097254'))
FILE_CHANNEL_LINK = environ.get('FILE_CHANNEL_LINK', 'https://t.me/Bullet_Data')

TMP_DOWNLOAD_DIRECTORY = environ.get("TMP_DOWNLOAD_DIRECTORY", "./DOWNLOADS/")
DOWNLOAD_LOCATION = environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/AudioBoT/")

# ────────────────────────── Miscellaneous ────────────────────────── #

COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "/")

SHORTLINK_URL = environ.get('SHORTLINK_URL', '')
SHORTLINK_API = environ.get('SHORTLINK_API', '')

GRP_LNK = environ.get('GRP_LNK', 'https://t.me/+k-0-OWAtrkoyM2Y1')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/+DIFevVBulGYzYzk1')
M_GRP_LINK = environ.get('M_GRP_LINK', 'https://t.me/+cft-rB6cc_o4OWFl')

VERIFY = is_enabled(environ.get('VERIFY', "False"), False)
IS_SHORTLINK = is_enabled(environ.get('IS_SHORTLINK', "False"), False)
NO_RESULTS_MSG = is_enabled(environ.get('NO_RESULTS_MSG', "False"), False)

DELETE_CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('DELETE_CHANNELS', '0').split()]
MAX_B_TN = environ.get("MAX_B_TN", "7")

MAX_BTN = is_enabled(environ.get('MAX_BTN', "False"), False)
PORT = environ.get("PORT", "8080")

MSG_ALRT = environ.get('MSG_ALRT', 'Piracy Is Crime')
NOR_ALRT = environ.get('NOR_ALRT', 'NO IMAGES IS FOUND')

LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001924870738'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'Nothing_Support_Group')

P_TTI_SHOW_OFF = is_enabled(environ.get('P_TTI_SHOW_OFF', "True"), True)
IMDB = is_enabled(environ.get('IMDB', "False"), False)
AUTO_FFILTER = is_enabled(environ.get('AUTO_FFILTER', "True"), True)
AUTO_DELETE = is_enabled(environ.get('AUTO_DELETE', "True"), True)
SINGLE_BUTTON = is_enabled(environ.get('SINGLE_BUTTON', "True"), True)

CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CUSTOM_FILE_CAPTION}")
CUSTOM_QUERY_CAPTION = environ.get("CUSTOM_QUERY_CAPTION", f"{script.CUSTOM_QUERY_CAPTION}")
CAPTION = environ.get("CAPTION", f"{script.CAPTION}")
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")

LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)

MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))

FILE_STORE_CHANNEL = [int(ch) for ch in environ.get('FILE_STORE_CHANNEL', '').split()]
MELCOW_NEW_USERS = is_enabled(environ.get('MELCOW_NEW_USERS', "True"), True)
PROTECT_CONTENT = is_enabled(environ.get('PROTECT_CONTENT', "False"), False)
PUBLIC_FILE_STORE = is_enabled(environ.get('PUBLIC_FILE_STORE', "True"), True)

# Redirect Links
MAIN_CHANNEL = environ.get('MAIN_CHANNEL', "https://t.me/+DIFevVBulGYzYzk1")
FILE_FORWARD = environ.get('FILE_FORWARD', "https://t.me/+hHHW8TOqFhE1OWQ1")

# Delete Time
IMDB_DLT_TIME = int(environ.get('IMDB_DLT_TIME', 600))
DLT_TIME = int(environ.get('DLT_TIME', 20))

# Heroku Config (optional)
HRK_APP_NAME = environ.get('HRK_APP_NAME', 'mybots')
HRK_API = environ.get('HRK_API', '0')

# ────────────────────────── Log Summary ────────────────────────── #

LOG_STR = "Current Customized Configurations are:-\n"
LOG_STR += ("IMDB Results enabled.\n" if IMDB else "IMDB Results disabled.\n")
LOG_STR += ("Redirect to /start enabled.\n" if P_TTI_SHOW_OFF else "Direct file sending enabled.\n")
LOG_STR += ("Single button mode enabled.\n" if SINGLE_BUTTON else "Dual button mode.\n")
LOG_STR += (f"Custom file caption: {CUSTOM_FILE_CAPTION}\n" if CUSTOM_FILE_CAPTION else "No custom file caption.\n")
LOG_STR += ("Long IMDB storyline enabled.\n" if LONG_IMDB_DESCRIPTION else "Short IMDB storyline.\n")
LOG_STR += ("Spell Check enabled.\n" if SPELL_CHECK_REPLY else "Spell Check disabled.\n")
LOG_STR += (f"Max list elements: {MAX_LIST_ELM}\n" if MAX_LIST_ELM else "No list element limit.\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}\n"
