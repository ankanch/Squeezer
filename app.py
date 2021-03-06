"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask, render_template, session, redirect, url_for, request, make_response
from functools import wraps
from webui import usermanager as UM
from webui import rulemanager as RM
from np_tools import  configmanager as CFGM
from np_tools import processwatch as PWATCH
import config as CFG


app = Flask(__name__)
app.secret_key = '238947uwJASOUD238UAOSDJAQ2ASD35482sad'

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "sid" in session.keys():
            if UM.checkSID(session["sid"]):
                return f(*args, **kwargs)
            return redirect(url_for('loginpage', next=request.url))
        sid = UM.generateSID()
        session["sid"] = sid
        return redirect(url_for('loginpage', next=request.url))
    return decorated_function


@app.route('/')
def index():
    if CFG.FIRST_SETUP:
        return redirect(url_for("setuppage"))
    return redirect(url_for("loginpage"))


@app.route('/login', methods=['GET', 'POST'])
def loginpage():
    if "sid" not in session.keys():
        sid = UM.generateSID()
        session["sid"] = sid
    if request.method != 'POST':
        if UM.checkSID(session["sid"]):
            return redirect(url_for("consolepage"))
        return render_template("login.html")
    else:
        try:
            if CFG.CONSOLE_PWD == request.form["password"]:
                UM.setLoggedSID(session["sid"])
                print("sid=", str(session["sid"]))
                return make_response(redirect(url_for("consolepage")))
        except Exception as e:
            print("login error:", e)
        return make_response(redirect(url_for("loginpage")))


@app.route('/consolehq')
@login_required
def consolepage():
    # get all rule data
    rules = RM.listrules()
    return render_template("console.html",
                           ruledata=rules,
                           email=CFG.EMAIL_RECIVIER,
                           apikey=CFG.SENDGRID_MAIL_API_KEY,
                           pushtime=CFG.EMAIL_SENDING_TIME.split(":"),
                           usertimezone=CFG.EMAIL_SENDING_TIMEZONE,
                           version=CFG.VERSION,
                           status_js=PWATCH.getServiceStatusHTML(PWATCH.SERVICE_JOB_SCHEDULER),
                           status_wi=PWATCH.getServiceStatusHTML(PWATCH.SERVICE_WEB_INTERFACE)
                           )


@app.route('/logout')
def logout():
    session["sid"] = "none"
    UM.logoutUser()
    return redirect(url_for("loginpage"))


@app.route('/setup')
def setuppage():
    if CFG.FIRST_SETUP:
        return render_template("setup.html",version=CFG.VERSION)
    return redirect(url_for('loginpage', next="console"))

@app.route('/api/firstsetup', methods=['POST'])
def api_firstsetup():
    if CFG.FIRST_SETUP:
        email = request.form["email"]
        time = request.form["time"]
        apikey = request.form["apikey"]
        password = request.form["password"]
        CFGM.changConfigure("email",email)
        CFGM.changConfigure("time",time)
        CFGM.changConfigure("apikey",apikey)
        CFGM.changConfigure("password",password)
        CFGM.changConfigure("first_setup", "False")
        return "success! please refresh this page." #make_response(redirect(url_for("loginpage"),code=307))
    return "error,you already setup Squeezer"


@app.route('/api/testrule', methods=['POST'])
@login_required
def api_testrule():
    retmsg = "empty"
    try:
        website = request.form["nr_site"]
        ruleset = request.form["nr_ruleset"]
        ret = RM.testRuleset(website, ruleset)
        retmsg = str("<br/>".join([news[0] for news in ret]))
    except Exception as e:
        retmsg = "error:" + str(e)
    return retmsg


@app.route('/api/delrule', methods=['POST'])
@login_required
def api_delrule():
    ruleid = request.form["ruleid"]
    return RM.removeRule(ruleid)


@app.route('/api/addrule', methods=['POST'])
@login_required
def api_addrule():
    rulename = request.form["nr_name"]
    website = request.form["nr_site"]
    ruleset = request.form["nr_ruleset"]
    return RM.addRule(rulename, website, ruleset)

@app.route('/api/updateinfo', methods=['POST'])
@login_required
def api_updatetime():
    infotype = request.form["infotype"]
    data = request.form["data"]
    CFGM.changConfigure(infotype,data)
    return "Success"

@app.route('/api/restartservice', methods=['POST'])
@login_required
def api_restartservice():
    sc = request.form["service_code"]
    PWATCH.restartService(int(sc))
    return "Success"

if __name__ == '__main__':
    #if PWATCH.checkService(PWATCH.SERVICE_WEB_INTERFACE):
    #    print("Squeezer>>>Web Interface already started.")
    #    exit()
    PWATCH.flagScriptRunning(PWATCH.SERVICE_WEB_INTERFACE)
    if CFG.DEBUG_MODE:
        app.run(host="127.0.0.1",port=1030,debug=True)
    else:
        app.run(host="0.0.0.0", port=1030)
    PWATCH.removeFlag(PWATCH.SERVICE_WEB_INTERFACE)
