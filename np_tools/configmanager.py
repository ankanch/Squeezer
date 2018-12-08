import config as CFG
import configparser

def changConfigure(key,value):
    keyname = ""
    if key == "email":
        CFG.EMAIL_RECIVIER = value
        keyname = "EMAIL_RECIVIER"
    elif key == "time":
        CFG.EMAIL_SENDING_TIME = value
        keyname = "EMAIL_SENDING_TIME"
    elif key == "apikey":
        CFG.SENDGRID_MAIL_API_KEY = value
        keyname = "SENDGRID_MAIL_API_KEY"
    elif key == "password":
        CFG.CONSOLE_PWD = value
        keyname = "console_password"
    elif key == "first_setup":
        CFG.FIRST_SETUP = False
        keyname = "first_setup"
    saveKey(keyname, value)
    return "Success"

def loadKey(key):
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config["Squeezer"][key]

def saveKey(key,value):
    config = configparser.ConfigParser()
    config.read('config.ini')
    config["Squeezer"][key] = value
    with open('config.ini',"w",encoding="utf-8") as f:
        f.truncate()
        config.write(f)