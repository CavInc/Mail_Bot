#-*- coding: utf-8 -*-
import email
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEBase
from email.mime.multipart import MIMEMultipart
__author__ = 'cav'

class SEND_MAIL:
    def __init__(self,server,user,password,ssl_mode=None,pop_port='default'):
        if ssl_mode==None:
            self.mp = smtplib.SMTP()
        else :
            self.mp = smtplib.SMTP_SSL()
        self.mp.connect(server)
        self.mp.login(user,password)

        pass

    def quit(self):
        self.mp.quit()

    def send(self,from_send,to_send,subject,data):
        msg = MIMEText(data, "", "utf-8")
        msg['Subject'] = subject
        msg['From'] = from_send
        msg['To'] = to_send
        self.mp.sendmail(from_send, [to_send], msg.as_string())
        pass

    def sendSrc(self,from_send,subject,data):
        pass

    pass