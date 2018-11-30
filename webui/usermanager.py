import uuid
import config as CFG

def generateSID():
    return str(uuid.uuid4())

def setLoggedSID(sid):
    with open("cache/user.logged","w") as f:
        f.truncate()
        f.write(str(sid))

def logoutUser():
    with open("cache/user.logged","w") as f:
        f.truncate()

def getLoggedSID():
    with open("cache/user.logged") as f:
        return f.read().replace("\n","")

def checkSID(sid):
    print(sid,getLoggedSID())
    if sid == getLoggedSID():
        return True
    return False

def updatePassword(newpass):
    CFG.CONSOLE_PWD = newpass
    with open("cache/WebUI.Password","w") as f:
        f.truncate()
        f.write(CFG.CONSOLE_PWD)
        return True
    return False