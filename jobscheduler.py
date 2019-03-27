import time,os, datetime,sys
from np_newsextractor.ruleset import ruleset
from np_newsextractor.rsinterpreter import executeRuleset
from np_newspusher.SendMail import sendMail,makeupNewsList
from np_tools.newscache import newscache
import config as CFG
from np_tools import commandmanager
from subprocess import Popen
from np_tools import processwatch as PWATCH

bypasscheck = False

def checkschdule():
    while True:
        # check every 1 minutes
        # get current time
        ct = datetime.datetime.now().strftime('%H:%M')
        if ct[:2] == CFG.EMAIL_SENDING_TIME[:2]  or bypasscheck:
            if int(ct[3:]) - int(CFG.EMAIL_SENDING_TIME[3:]) <= 0 or bypasscheck:
                time.sleep(65)
                break
        time.sleep(55)
    return True

def runTask():
    nl = []
    tasklist = os.listdir("schduled_rulesets/")
    for task in tasklist:
        if len(task) > 2:
            # load task ruleset
            rs = ruleset()
            rs.importRules(dir= "schduled_rulesets/" + task)
            # perform task
            print("executing rule for ",rs.name, rs.site)
            data = executeRuleset(rs)
            nl.extend(data)
    return nl

def pushNews(nl):
    data = makeupNewsList(nl)
    sendMail("squeezer@akakanch.com",CFG.EMAIL_RECIVIER,"Squeezer:News of the day",data)

def runScheduler():
    print("runScheduler():Squeezer Job Scheduler Running.Schedule push time is ", CFG.EMAIL_SENDING_TIME)
    nc = newscache()
    nc.load()
    while True and commandmanager.checkCommand(commandmanager.COMMAND_RUN_SCHEDULER):
        if checkschdule():
            try:
                nl = runTask()
                nl = nc.filternews(nl)
                pushNews(nl)
                bypasscheck = False
                print("news pushed")
            except:
                bypasscheck = True
                print("error in grab or push, bypass check for once.")
                time.sleep(10)
    print("runScheduler(): COMMAND_RUN_SCHEDULER not detected! Exit.")

def performTask():
    print("performTask():Start grabbing and pushing ")
    nc = newscache()
    nc.load()
    finsiehd  = False
    max_try = 10
    tried = 1
    while finsiehd == False and tried <= max_try:
        try:
            nl = runTask()
            nl = nc.filternews(nl)
            pushNews(nl)
            print("performTask():news pushed")
            finsiehd = True
        except Exception as e:
            print("performTask(): error occurred. retry in 15 seconds.",e)
            time.sleep(15)
            tried += 1
    return finsiehd

def checkTime():
    """
    as long as minute matched, True will be returned
    :return: True, if minute matched
    """
    ct = datetime.datetime.now().strftime('%H:%M')
    if ct == CFG.EMAIL_SENDING_TIME:
        return True
    return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        #runScheduler()
        performTask()
    else:
        print("jobscheduler.py:Scheduler Started ")
        PWATCH.flagScriptRunning(PWATCH.SERVICE_JOB_SCHEDULER)
        while True:
            print("jobscheduler.py:check time ")
            if checkTime():
                if commandmanager.checkCommand(commandmanager.COMMAND_RUN_SCHEDULER):
                    print("jobscheduler.py:ready to send,waiting 60 seconds")
                    time.sleep(60)
                    if performTask() == False:
                        print("failed to push news, restarting Squeezer... ")
                        commandmanager.removeCommand(commandmanager.COMMAND_RUN_SCHEDULER)
                        commandmanager.addCommand(commandmanager.COMMAND_RESTART_SCHEDULER)
            time.sleep(10)
            if commandmanager.checkCommand(commandmanager.COMMAND_RESTART_SCHEDULER):
                commandmanager.removeCommand(commandmanager.COMMAND_RESTART_SCHEDULER)
                break
        print("jobscheduler.py:Scheduler Stopped.")
        PWATCH.removeFlag(PWATCH.SERVICE_JOB_SCHEDULER)
        sys.exit(commandmanager.SCHEDULER_EXIT_CODE)
