#!/usr/bin/python
#-*- coding:utf-8 -*-
from email_wrk.post_email import *
from email_wrk.glu import LoadCFG,getConfig,getPOPConfig,getIMAPConfig,LoadFilter,getSMTP
from email_wrk.work_filter import Work_filter

__author__ = 'cav'

if __name__=='__main__':
    LoadCFG('config.ini')
    LoadFilter(getConfig()['filter'])
    print 'ПРИВЕТ'
    print getConfig()
    if getConfig()['mail_mode']=='POP':
        print getPOPConfig()['ssl']=='yes'
        post = POST_EMAIL(getPOPConfig()['host'],getPOPConfig()['user'],getPOPConfig()['pass'],
                          mode=POST_MODE_POP,ssl_mode=(getPOPConfig()['ssl']=='yes'))
        Work_filter(post,LoadFilter(getConfig()['filter']),filter_name=getConfig()['filter_name'],
                    smtp_conf=getSMTP())

    if getConfig()['mail_mode']=='IMAP':
        post = POST_EMAIL(getIMAPConfig()['host'],getIMAPConfig()['user'],getIMAPConfig()['pass'],
                          mode=POST_MODE_IMAP,ssl_mode=(getIMAPConfig()['ssl'] == 'yes'))
        Work_filter(post,LoadFilter(getConfig()['filter']),filter_name=getConfig()['filter_name'],
                    smtp_conf=getSMTP())

    post.quit()


