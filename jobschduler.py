import time,os, datetime
from np_newsextractor.ruleset import ruleset
from np_newsextractor.rsinterpreter import executeRuleset
from np_newspusher.SendMail import sendMail,makeupNewsList
import config as CFG

def checkschdule():
    while True:
        # check every 5 minutes
        # get current time
        ct = datetime.datetime.now().strftime('%H:%M')
        if ct[:2] == CFG.EMAIL_SENDING_TIME[:2]:
            if int(ct[3:]) - int(CFG.EMAIL_SENDING_TIME[3:]) <= 0:
                time.sleep(120)
                print("time is up.")
                break
        time.sleep(55)
        print("not ready")
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
    sendMail("squeezer@akakanch.com",CFG.EMAIL_RECIVIER,"title",data)

if __name__ == "__main__":
    print("Squeezer Job Scheduler Running")
    while True:
        if checkschdule():
            nl = runTask()
            pushNews(nl)
            print("news pushed")
