from np_tools.loadconfidentials import loadConfidential

# email api key
SENDGRID_MAIL_API_KEY = loadConfidential("confidentials/SendGridAPIKey.txt")

# email preference
EMAIL_SENDING_TIME = "21:42"     # in UTC+0
EMAIL_RECIVIER = "1075900121@qq.com"

# web UI preference
CONSOLE_PWD = ""

# news cache
MAX_CACHED_NEWS = 1000

# squeezer source
VERSION = "0.1"