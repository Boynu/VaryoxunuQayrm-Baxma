class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 12210813
    API_HASH = "e42eeae11a2f96bcfc5ec3b46a30adad"

    CASH_API_KEY = "UBL5Z9KSLQU7WJ41"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://bsatebmuxxtgdp:1af90c44e2514cc3172bf1af3501528841478d39a5efd132816a8e7366d96b2d@ec2-54-90-13-87.compute-1.amazonaws.com:5432/dbvpgskodfoi1l"  # A sql database url from elephantsql.com

    EVENT_LOGS = "-1002021260760"  # Event logs channel to note down important bot level events
    
    MONGO_DB_URI =   "mongodb+srv://music:music@cluster0.sh6h4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com
    
    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://telegra.ph/file/7cbc16a9c922358dff2d9.jpg"

    SUPPORT_CHAT = "Kayfina"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "5890868081:AAGuNeGAOz5A1DuEBQ8OqZE_Q1tJLqxOGo4"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "ZGUEKKT6B5ZL"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 5663585448  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
