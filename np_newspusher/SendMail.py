import sendgrid
import os
import config as npconfig
from sendgrid.helpers.mail import *

sg = sendgrid.SendGridAPIClient(apikey=npconfig.SENDGRID_MAIL_API_KEY)


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

def makeupNewsList():
    pass


if __name__ == "__main__":
    sendMail("test@akakanch.com", "kanchisme@gmail.com", "this is a test email", "test contenct here")