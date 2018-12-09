from subprocess import Popen
import time,datetime
from np_tools import commandmanager as cmdmgr

def startScheduler():
    cmdmgr.addCommand(cmdmgr.COMMAND_RUN_SCHEDULER)

def stopScheduler():
    cmdmgr.removeCommand(cmdmgr.COMMAND_RUN_SCHEDULER)

def restartScheduler():
    cmdmgr.addCommand(cmdmgr.COMMAND_RESTART_SCHEDULER)

if __name__ == "__main__":
    p = Popen("python jobscheduler.py run as production env", shell=True)
    cmdmgr.addCommand(cmdmgr.COMMAND_RUN_SCHEDULER)
    while True:
        statuscode = p.poll()
        if statuscode == cmdmgr.SCHEDULER_EXIT_CODE:
            print("scheduler_interface.py:Restarting....")
            p = Popen("python jobscheduler.py run as production env", shell=True)
        else:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"|scheduler_interface.py: running fine")
            time.sleep(5)
