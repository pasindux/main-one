import os

class Config():
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    # The Telegram API things
    API_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")
    # Get these values from my.telegram.org
    # Array to store users who are authorized to use the bot

    # file /video dpwnload location
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    OWNER_ID = os.environ.get("OWNER_ID") # Your(owner's) telegram id
    #If deploying on vps edit the above value as example := OWNER_ID = Your-telegram id-without-inverted-commas
    
    REDIS_URI = os.environ.get("REDIS_URI", "None") # Get This Value from http://redislabs.com/try-free (If you don't know how to obtain the a video tutorial is available here:- https://t.me/botzupdate/5)
    #If deploying on vps edit the above value as example := REDIS_URI = "Your-Redis-Endpoint-inside-inverted-commas."
    
    REDIS_PASS = os.environ.get("REDIS_PASS", "None")
    # Telegram maximum file upload size
    TG_MAX_FILE_SIZE = 4194304000

    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")

    # set timeout for subprcess
    PROCESS_MAX_TIMEOUT = 3700

    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -100))
    OWNER_ID = int(os.environ.get("OWNER_ID", "12356"))
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    ADL_BOT_RQ = {}
    AUTH_USERS = list({int(x)
                      for x in os.environ.get("AUTH_USERS", "0").split()})
    AUTH_USERS.append(OWNER_ID)
