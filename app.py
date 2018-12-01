from flask import Flask, render_template, session, redirect, url_for, request, make_response
from functools import wraps
from webui import usermanager as UM
from webui import rulemanager as RM
import config as CFG

app = Flask(__name__)
app.secret_key = '238947uwJASOUD238UAOSDJAQ2ASD35482sad'


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
    return render_template("index.html")


@app.route('/login', methods=['GET', 'POST'])
def loginpage():
    if request.method != 'POST':
        if UM.checkSID(session["sid"]):
            return redirect(url_for("consolepage"))
        return render_template("login.html")
    else:
        try:
            if CFG.CONSOLE_PWD == request.form["password"]:
                UM.setLoggedSID(session["sid"])
                print("sid=", str(session["sid"]))
                return make_response(redirect("console"))
        except Exception as e:
            print("login error:", e)
        return make_response(redirect("login"))


@app.route('/console')
@login_required
def consolepage():
    # get all rule data
    rules = RM.listrules()
    return render_template("console.html", ruledata=rules, email=CFG.EMAIL_RECIVIER, apikey=CFG.SENDGRID_MAIL_API_KEY)


@app.route('/logout')
def logout():
    session["sid"] = "none"
    UM.logoutUser()
    return redirect(url_for("loginpage"))


@app.route('/setup')
def setuppage():
    if CFG.FIRST_SETUP:
        return render_template("setup.html")
    return redirect(url_for('loginpage', next="console"))


@app.route('/api/testrule', methods=['POST'])
@login_required
def api_testrule():
    rulename = request.form["nr_name"]
    website = request.form["nr_site"]
    fkey = request.form["nr_key"]
    igchild = request.form["nr_igchild"]
    selectos = request.form["nr_selectors"]
    return rulename


@app.route('/api/addrule', methods=['POST'])
@login_required
def api_addrule():
    rulename = request.form["nr_name"]
    website = request.form["nr_site"]
    fkey = request.form["nr_key"]
    igchild = request.form["nr_igchild"]
    selectos = request.form["nr_selectors"]
    return rulename


if __name__ == '__main__':
    app.run()
