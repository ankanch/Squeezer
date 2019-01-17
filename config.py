from np_tools.loadconfidentials import loadConfidential
from np_tools.configmanager import loadKey

# web UI preference
CONSOLE_PWD = loadKey("console_password")
FIRST_SETUP = eval(loadKey("FIRST_SETUP"))

# others
DEBUG_MODE = eval(loadKey("DEBUG_MODE"))


# email api key
SENDGRID_MAIL_API_KEY = ""
if DEBUG_MODE:
    SENDGRID_MAIL_API_KEY = loadConfidential("confidentials/SendGridAPIKey.txt")
    FIRST_SETUP = False
else:
    SENDGRID_MAIL_API_KEY = loadKey("sendgrid_mail_api_key")

# email preference
EMAIL_SENDING_TIME = loadKey("EMAIL_SENDING_TIME")     # in UTC+0
EMAIL_RECIVIER = loadKey("EMAIL_RECIVIER")

# news cache
MAX_CACHED_NEWS = eval(loadKey("MAX_CACHED_NEWS"))

# squeezer source fixed
SPIDER_UA = "Mozilla/5.0"
VERSION = "ver 0.1 @ 2018"
