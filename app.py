from flask import Flask,render_template,session,redirect,url_for,request,make_response
from functools import wraps
from webui import  usermanager as UM
import config as CFG

app = Flask(__name__)
app.secret_key = '238947uwJASOUD238UAOSDJAQ2ASD35482sad'

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "sid" in session.keys():
            if UM.checkSID(session["sid"]):
                return render_template("console.html")
            return redirect(url_for('loginpage', next=request.url))
        sid = UM.generateSID()
        session["sid"] = sid
        return redirect(url_for('loginpage', next=request.url))
    return decorated_function

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login',methods=['GET', 'POST'])
def loginpage():
    if request.method != 'POST':
        if UM.checkSID(session["sid"]):
            return redirect(url_for("consolepage"))
        return render_template("login.html")
    else:
        try:
            if CFG.CONSOLE_PWD == request.form["password"]:
                UM.setLoggedSID(session["sid"])
                print("sid=",str(session["sid"]))
                return make_response(redirect("console"))
        except Exception as e:
            print("login error:",e)
        return make_response(redirect("login"))

@app.route('/console')
@login_required
def consolepage():
    return render_template("console.html")

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

if __name__ == '__main__':
    app.run()
