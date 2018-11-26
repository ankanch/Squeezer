import time,os, datetime
from np_newsextractor.ruleset import ruleset
from np_newsextractor.rsinterpreter import executeRuleset
from np_newspusher.SendMail import sendMail,makeupNewsList
import config as CFG

bypasscheck = False

def checkschdule():
    while True:
        # check every 1 minutes
        # get current time
        ct = datetime.datetime.now().strftime('%H:%M')
        if ct[:2] == CFG.EMAIL_SENDING_TIME[:2]  or bypasscheck:
            if int(ct[3:]) - int(CFG.EMAIL_SENDING_TIME[3:]) <= 0 or bypasscheck:
                time.sleep(65)
                print("time is up.")
                break
        print("not ready")
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

if __name__ == "__main__":
    print("Squeezer Job Scheduler Running")
    print("schedule push time is ", CFG.EMAIL_SENDING_TIME)
    while True:
        if checkschdule():
            try:
                nl = runTask()
                pushNews(nl)
                bypasscheck = False
                print("news pushed")
            except:
                bypasscheck = True
                print("error in grab or push, bypass check for once.")
                time.sleep(10)

