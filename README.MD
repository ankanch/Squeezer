## Squeezer
A news grabber and pusher. Including a web interface to manage grab rules. The framework is using [SendGrid](https://sendgrid.com/) to push news.

### Deployment Environment

* Windows Server 2008/2012/2016 with Python 3.6+
* Windows 8/10 with Python 3.6+

### How to
* Step 1: Download source from release to somewhere on your server.
* Step 2: Enter Squeezer folder and run cmd `virtualenv venv` to set up a [Python virtual environment](https://programwithus.com/learn-to-code/Pip-and-virtualenv-on-Windows/), then activating it by `.\env\Scripts\activate`. After that, you can install required Python packages from `requirements.txt`. **You can do this in a easier way, just run `setup_env.bat` in command prompt, we will set the environment for you.**
* Step 3: Run cmd `.\start_squeezer.bat` to start Squeezer service.
* Step 4: Visit `http://your-server-ip:1030` to configure Squeezer. (You have to sign up a [SendGrid](https://sendgrid.com/) account to send email.)
* Step 5: Add your own rules in Squeezer console, then you are all done. Desigend updates will be send to your email directly.

_Two sample rulesets has been placed in `schduled_rulesets` folder._

### Screenshots

![console img](https://github.com/ankanch/Squeezer/blob/master/static/readmeimg/console-welcome-section.jpg)


