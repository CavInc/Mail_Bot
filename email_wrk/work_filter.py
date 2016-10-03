#-*- coding:utf-8 -*-
import re
from email_wrk.send_email import SEND_MAIL
__author__ = 'cav'

'''
 Обработка фильтрами
'''

no_work_num=()

# стурктура для оправки
send_post={}

def Work_filter(post,filter_rec,filter_mode='single',filter_name=None,smtp_conf=None):
    print filter_rec
    filter = filter_rec[filter_name]


    header = post.getHeader()

    for id in header:
        if filter['filter_param_option']=='first' :
            if header[id]['from'].upper().find(filter['filter_from'].upper()) != -1:
                print id
                __run(id,post,filter,header,smtp_conf=smtp_conf)
                pass
            pass
        if filter['filter_param_option']=='last':
            if header[id]['from'].upper().find(filter['filter_subject'].upper()) != -1:
                print id
                pass
            pass
        if filter['filter_param_option']=='and':
            if header[id]['from'].find(filter['filter_from'])!=-1 and header[id]['from'].upper().find(filter['filter_subject'].upper()) != -1:
                print id

                pass
            pass
        if filter['filter_param_option']=='or':
            pass

    pass

# возвращаем ключи операций
def __getOperation(val):
    def f(x):
        if x.find('filter_function_')!=-1:
            return True
        return False
    return filter(f,val.keys())
    pass

filter_work_word = ('del_format' , 'del_hiperlink', 'del_in_start_word', 'del_body_mail', 'set_subject',
                    'del_body_word','change_word_subject', 'send_attachments', 'no_onwer_filter')

# обрабатываем писмо по правилам
def __run(id,post,filter_work,header,smtp_conf=None):
    key_operation=__getOperation(filter_work)
    print key_operation
    data = post.getMessage(id)
    print data
    for key in key_operation:
        if key.find('filter_function_')!=-1:
            print filter_work[key]
            if filter_work[key]=='del_hiperlink':
                data = __del_hiperlink(data)
                send_post['body']=data
                pass

            if filter_work[key]=='del_format':
                pass

            if filter_work[key]=='set_subject':
                subj = __set_subject(filter_work,key)
                __send_post(header[id]['from'],header[id]['to'],subj,data,smtp_conf)
                pass

            if filter_work[key]=='del_in_start_word':
                pass

            if filter_work[key]=='change_word_subject':
                pass


    pass

# удаляем ссылки
def __del_hiperlink(data):
    return re.sub(r'(http[s]??:\/\/)?([\da-z\,-]+)\.([a-z\.]{2,6})([\/\w\.-]*)\/?', '', data)
    pass

# смена subject
def __set_subject(filter,key):
    num_key= key[key.rfind('_')+1:]
    return  filter['filter_option_'+num_key]

# отправка почты
def __send_post(from_send,to_send,subj,data,smtp_conf):
    send = SEND_MAIL(smtp_conf['host'],smtp_conf['user'],smtp_conf['pass'],ssl_mode=(smtp_conf['ssl']=='yes'))
    send.send(from_send,to_send,subj,data)
    send.quit()
    pass