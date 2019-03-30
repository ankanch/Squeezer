import config as CFG
import datetime
from time import gmtime, strftime
import configparser

def convertTime(giventime,timezone):
    """
    [UTC TIMEZONE ONLY]
    convert user given time and timezone to local machine time
    :param giventime: given mail delivery time like HH:MM
    :param timezone: given preferred  timezone like +8
    :return: local machine time
    """
    # get local machine timezone (LMT)
    lmt = strftime("%z", gmtime())[:3]
    ilmt = int(lmt)

    # get user timezone (UT)
    ut = timezone[3:]
    iut = int(ut)

    # converse
    gap = iut - ilmt
    hh = int(giventime[:2])
    hh += gap
    if hh >= 24:
        hh -= 24
    if hh < 0:
        hh += 24
    return str(hh) + giventime[2:]

def changConfigure(key,value):
    keyname = ""
    if key == "email":
        CFG.EMAIL_RECIVIER = value
        keyname = "EMAIL_RECIVIER"
    elif key == "time":
        timedata = value.split("@")
        value = convertTime(timedata[0],timedata[1])
        if len(value) < 5:
            value = "0" + value
        CFG.EMAIL_SENDING_TIME = value
        CFG.EMAIL_SENDING_TIMEZONE = timedata[1]
        saveKey("EMAIL_SENDING_TIMEZONE",timedata[1])
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