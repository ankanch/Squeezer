import time,os, datetime
from np_newsextractor.ruleset import ruleset
from np_newsextractor.rsinterpreter import executeRuleset
from np_newspusher.SendMail import sendMail,makeupNewsList
from np_tools.newscache import newscache
import config as CFG
from np_tools import commandmanager

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
    print("started.")
    while True and commandmanager.checkCommand(CFG.COMMAND_RUN_SCHEDULER):
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

if __name__ == "__main__":
    runScheduler()
