import psutil
import os
import sys

SERVICE_JOB_SCHEDULER = 0
SERVICE_WEB_INTERFACE = 1
SERVICE_SERVICE_WATCH = 2

SERVICE_NAME_LIST = ["JOB_SCHEDULER_",
                     "WEB_INTERFACE_",
                     "SERVICE_WATCH_",
                     ]

SERVICE_STARTCMD_LIST = [
                            ".\start_jobscheduler.bat",
                            ".\start_webinterface.bat",
                            "",
                        ]

def checkIfProcessRunning(pid):
    '''
    Check if there is any running process that contains the given pid.
    '''
    print(pid)
    if psutil.pid_exists(pid):
        return True
    return False

def checkService(service_code):
    """
    use this function to check if a python script is running
    return ture if running
    """
    service_name = SERVICE_NAME_LIST[service_code];
    flist = os.listdir("cache/")
    for f in flist:
        pos = f.find(service_name)
        if pos > 0:
            return checkIfProcessRunning( int( f[pos + len(service_name):] ))
    return False

def flagScriptRunning(service_code):
    pid = str(os.getpid())
    pidfile = "cache/SERVICE_" + SERVICE_NAME_LIST[service_code] + pid
    open(pidfile, 'w').write(pid)

def removeFlag(service_code):
    flist = os.listdir("cache/")
    for f in flist:
        if f.find(SERVICE_NAME_LIST[service_code]) > 0:
            os.remove("cache/" + f)


def getServiceStatusHTML(service_code):
    if checkService(service_code):
        return """<span class="badge badge-success">Running</span>"""
    return """<span class="badge badge-danger">Stopped</span>"""

def getRunningServicePID(service_code):
    service_name = SERVICE_NAME_LIST[service_code];
    flist = os.listdir("cache/")
    for f in flist:
        pos = f.find(service_name)
        if pos > 0:
            return int( f[pos + len(service_name):] )

def restartService(service_code):
    #if service_code == SERVICE_JOB_SCHEDULER:
    #    CMDMGR.addCommand(CMDMGR.COMMAND_RESTART_SCHEDULER)
    #os.system(SERVICE_STARTCMD_LIST[service_code])
    pass

if __name__ == "__main__":
    #print("TEST>>>Web Interface Status:",checkService(SERVICE_WEB_INTERFACE))
    restartService(SERVICE_JOB_SCHEDULER)