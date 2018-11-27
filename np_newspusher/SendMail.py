import datetime

import sendgrid
import os
import config as npconfig
from sendgrid.helpers.mail import *

sg = sendgrid.SendGridAPIClient(apikey=npconfig.SENDGRID_MAIL_API_KEY)

mailtemp = """
            <div style="text-align: left;"><i>Today is @DATETIME. You have @NCOUNT news to read.</i></div>
            <div style="text-align: left;"><i>Here're the news of the day.</i></div>
            <div style="text-align: left;">================================</div>
            <div style="text-align: left;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;NEWS OF THE TODAY</div>
            <div style="text-align: left;">================================</div>
            <font face="黑体" style="" size="2">@NEWSLIST</font>
            <div style="text-align: left;">================================</div>
            <div style="text-align: left;"><font size="1"><i>News above were generated at @GENTIME on this day.</i></font></div>
            <div style="text-align: left;">
                <font size="1"><i>This email is sent by 
                <a href="https://github.com/ankanch/Squeezer">squeezer</a>
                &nbsp;(@VERSION), a news grabber and pusher framework.</i>
                <span style="color: rgb(0, 128, 128); font-weight: bold; font-family: SimSun; white-space: pre-wrap;"></span>
                </font>
            </div>
            <div><br></div>
            """

newstemp = """<a href="@LINK" style="">-@TITLE</a><br>"""

def sendMail(fs, to, title, mcontent):
    from_email = Email(fs)
    to_email = Email(to)
    subject = title
    content = Content("text/html", mcontent)
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    ret = "status code : " + str(response.status_code) + "<br/>response body : " + str(response.body)
    ret += "<br/>response headers : " + str(response.headers)
    return ret

def makeupNewsList(nl):
    data = ""
    now = datetime.datetime.now()
    todaystr = now.strftime("%Y-%m-%d")
    gentime = now.strftime("%H:%M")
    for news in nl:
        data += newstemp.replace("@LINK",news[1]).replace("@TITLE",news[0])
    newmail = mailtemp.replace("@DATETIME",todaystr)\
            .replace("@GENTIME",gentime)\
            .replace("@NEWSLIST",data)\
            .replace("@VERSION",npconfig.VERSION)\
            .replace("@NCOUNT",str(len(nl)))
    return newmail


if __name__ == "__main__":
    sendMail("squeezer@akakanch.com", "1075900121@qq.com", "this is a test email", "test contenct here")