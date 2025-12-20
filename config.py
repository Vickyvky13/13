import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

def get_int(name, default=None, required=False):
    value = getenv(name)
    if value is None or value == "":
        if required and default is None:
            raise SystemExit(f"[CONFIG ERROR] {name} is missing")
        return default
    try:
        return int(value)
    except ValueError:
        raise SystemExit(f"[CONFIG ERROR] {name} must be an integer")

def get_str(name, default=None, required=False):
    value = getenv(name)
    if value is None or value == "":
        if required and default is None:
            raise SystemExit(f"[CONFIG ERROR] {name} is missing")
        return default
    return value


# ===================== REQUIRED TELEGRAM CONFIG =====================

API_ID = get_int("API_ID", 13569561, required=True)
API_HASH = get_str("API_HASH", "a689fce8b9f1c32c899b53811451385f", required=True)
BOT_TOKEN = get_str("BOT_TOKEN", required=True)

# ===================== DATABASE =====================

MONGO_DB_URI = get_str("MONGO_DB_URI")

# ===================== BASIC SETTINGS =====================

DURATION_LIMIT_MIN = get_int("DURATION_LIMIT", 60)
LOG_GROUP_ID = get_int("LOG_GROUP_ID", -1003454537656)
OWNER_ID = get_int("OWNER_ID", 8360539783)

# ===================== HEROKU / DEPLOY =====================

HEROKU_APP_NAME = get_str("HEROKU_APP_NAME")
HEROKU_API_KEY = get_str("HEROKU_API_KEY")

# ===================== API SERVICES =====================

API_URL = get_str("API_URL", "https://api.nexgenbots.xyz")
VIDEO_API_URL = get_str("VIDEO_API_URL", "https://api.video.nexgenbots.xyz")
API_KEY = get_str("API_KEY")

# ===================== GIT =====================

UPSTREAM_REPO = get_str(
    "UPSTREAM_REPO",
    "https://github.com/CyberPixelPro/AviaxMusic"
)
UPSTREAM_BRANCH = get_str("UPSTREAM_BRANCH", "master")
GIT_TOKEN = get_str("GIT_TOKEN")

# ===================== SUPPORT =====================

SUPPORT_CHANNEL = get_str("SUPPORT_CHANNEL", "https://t.me/NexGenBots")
SUPPORT_GROUP = get_str("SUPPORT_GROUP", "https://t.me/NexGenBotsIndia")

AUTO_LEAVING_ASSISTANT = bool(int(getenv("AUTO_LEAVING_ASSISTANT", "0")))
PRIVACY_LINK = get_str(
    "PRIVACY_LINK",
    "https://telegra.ph/Privacy-Policy-for-AviaxMusic-08-14"
)

# ===================== SPOTIFY =====================

SPOTIFY_CLIENT_ID = get_str("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = get_str("SPOTIFY_CLIENT_SECRET")

# ===================== LIMITS =====================

PLAYLIST_FETCH_LIMIT = get_int("PLAYLIST_FETCH_LIMIT", 25)
TG_AUDIO_FILESIZE_LIMIT = get_int("TG_AUDIO_FILESIZE_LIMIT", 104857600)
TG_VIDEO_FILESIZE_LIMIT = get_int("TG_VIDEO_FILESIZE_LIMIT", 2145386496)

# ===================== STRING SESSIONS =====================

STRING1 = get_str("STRING_SESSION")
STRING2 = get_str("STRING_SESSION2")
STRING3 = get_str("STRING_SESSION3")
STRING4 = get_str("STRING_SESSION4")
STRING5 = get_str("STRING_SESSION5")

# ===================== GLOBALS =====================

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# ===================== IMAGES =====================

START_IMG_URL = get_str("START_IMG_URL", "https://files.catbox.moe/dkyy20.jpg")
PING_IMG_URL = get_str("PING_IMG_URL", "https://graph.org/file/389a372e8ae039320ca6c.png")

PLAYLIST_IMG_URL = "https://graph.org/file/3dfcffd0c218ead96b102.png"
STATS_IMG_URL = "https://graph.org/file/99a8a9c13bb01f9ac7d98.png"
TELEGRAM_AUDIO_URL = "https://graph.org/file/2f7debf856695e0ef0607.png"
TELEGRAM_VIDEO_URL = "https://graph.org/file/2f7debf856695e0ef0607.png"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/2f7debf856695e0ef0607.png"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


# ===================== TIME =====================

def time_to_seconds(time):
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(str(time).split(":"))))

DURATION_LIMIT = time_to_seconds(f"{DURATION_LIMIT_MIN}:00")

# ===================== URL VALIDATION =====================

if SUPPORT_CHANNEL and not re.match(r"^https?://", SUPPORT_CHANNEL):
    raise SystemExit("[ERROR] SUPPORT_CHANNEL must start with https://")

if SUPPORT_GROUP and not re.match(r"^https?://", SUPPORT_GROUP):
    raise SystemExit("[ERROR] SUPPORT_GROUP must start with https://")