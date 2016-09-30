#-*- coding: utf-8 -*-
import email
import smtplib
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

    def send(self,from_send,subject,data):
        pass

    pass