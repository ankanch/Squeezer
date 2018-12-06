import os

PATH_TO_COMMAND = "cache/"

def checkCommand(cmd):
    cmdlist = os.listdir(PATH_TO_COMMAND)
    if cmd in cmdlist:
        return True
    return False

def addCommand(cmdtype):
    with open(PATH_TO_COMMAND + cmdtype,"w") as f:
        f.write("this is a command file of Squeezer")

def removeCommand(cmdtype):
    os.remove(PATH_TO_COMMAND + cmdtype)