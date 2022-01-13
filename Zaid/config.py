# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = "6850612"  
    API_HASH = "dfde10a379b6b08184bf6c8966aece3b"
    TOKEN = "5090796273:AAFMvj6w5lHzSsSVgz6NV8rz83WQMUKBWmI"
    OWNER_ID = "5058700158"
    OWNER_USERNAME = "iam_dixie"
    MONGO_DB_URI = "mongodb+srv://Kishan:7701800@cluster0.cefre.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    SUPPORT_CHAT = "the_arc_support"
    JOIN_LOGGER = "-1001664982598"
    EVENT_LOGS = "-1001664982598"

    # RECOMMENDED
    INFOPIC = "https://telegra.ph/file/1331a79a2fa3256a3b67a.jpg"   
    CF_API_KEY = ""
    LASTFM_API_KEY = ""
    BOT_USERNAME = "arc_robot"
    WALL_API = ""
    OPENWEATHERMAP_ID = ""
    TEMP_DOWNLOAD_DIRECTORY = ""
    REM_BG_API_KEY = ""
    TIME_API_KEY = ""
    CASH_API_KEY = ""
    REM_BG_API_KEY = ""
    SESSION_STRING = "1AZWarzMBu7HBEj6owjUULuklhtXZMGE4gWOlK3Ba93y2C4NtzQyCgF9_1Kpn9oPlZ_0kR7Nw3ValKS9ODePC-FYhvYTFHh5UhgOSekgastUtRBGSJ7DvV-Tq6Pk6FeQD_ea07s2QSVfwRCYWvViLMAbkvdurbUsAoSdqxKJDAWTcDwXdYCMxWxzVxHxaoHhtOErsTs6BBBdLo9nQ6EzkcuanPiw8PiDw5D8KEWonUD1d5D9j0LWEnBgujr2Fpep_ijcGHr6rotvtizBxTbfd3KrjunoQsI1d9G5TF_2txVmbMvEJFGGnLWKySSEzzgw2RIq0fGpNlHRTuwtjIIoOR_iAia4Heig="
    ARQ_API_KEY = "UIUXOY-NTKWDC-QHFFMD-DHHKVV-ARQ"
    ARQ_API = "UIUXOY-NTKWDC-QHFFMD-DHHKVV-ARQ"
    ARQ_API_URL = "aww"
    HEROKU_APP_NAME = ""
    HEROKU_API_KEY = ""
    BOT_ID = "5090796273"
    STRING_SESSION = "1AZWarzMBu7HBEj6owjUULuklhtXZMGE4gWOlK3Ba93y2C4NtzQyCgF9_1Kpn9oPlZ_0kR7Nw3ValKS9ODePC-FYhvYTFHh5UhgOSekgastUtRBGSJ7DvV-Tq6Pk6FeQD_ea07s2QSVfwRCYWvViLMAbkvdurbUsAoSdqxKJDAWTcDwXdYCMxWxzVxHxaoHhtOErsTs6BBBdLo9nQ6EzkcuanPiw8PiDw5D8KEWonUD1d5D9j0LWEnBgujr2Fpep_ijcGHr6rotvtizBxTbfd3KrjunoQsI1d9G5TF_2txVmbMvEJFGGnLWKySSEzzgw2RIq0fGpNlHRTuwtjIIoOR_iAia4Heig="
    SQLALCHEMY_DATABASE_URI = "postgres://yzsbksct:N6jeVX_sQbqGp39ZVN524aSSuJz4iZGA@rosie.db.elephantsql.com/yzsbksct"
    DATABASE_URL = "postgres://yzsbksct:N6jeVX_sQbqGp39ZVN524aSSuJz4iZGA@rosie.db.elephantsql.com/yzsbksct"
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = ""  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = "2144966937"
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = "2144966937"
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = "2144966937"
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = "2144966937"
    WOLVES = "2144966937"
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    ALLOW_CHATS = True
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "awoo"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "awoo"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "awoo"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = "awoo"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
