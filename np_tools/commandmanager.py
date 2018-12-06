import os

SCHEDULER_EXIT_CODE = 100

COMMAND_RUN_SCHEDULER = "CMD_RUN_SCHEDULER.CMD"
COMMAND_RESTART_SCHEDULER = "CMD_RESTART_SCHEDULER.CMD"

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