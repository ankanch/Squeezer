from np_tools.loadconfidentials import loadConfidential
from np_tools.configmanager import loadKey

# email api key
SENDGRID_MAIL_API_KEY = loadConfidential("confidentials/SendGridAPIKey.txt")

# email preference
EMAIL_SENDING_TIME = loadKey("EMAIL_SENDING_TIME")     # in UTC+0
EMAIL_RECIVIER = loadKey("EMAIL_RECIVIER")

# web UI preference
CONSOLE_PWD = loadKey("console_password")
FIRST_SETUP = loadKey("FIRST_SETUP")

# news cache
MAX_CACHED_NEWS = loadKey("MAX_CACHED_NEWS")

# squeezer source
VERSION = "ver 0.1 @ 2018"
