#-*- coding:utf-8 -*-
import re
__author__ = 'cav'

'''
 Обработка фильтрами
'''

no_work_num=()

def Work_filter(post,filter_rec,filter_mode='single',filter_name=None):
    print filter_rec
    filter = filter_rec[filter_name]


    header = post.getHeader()

    for id in header:
        if filter['filter_param_option']=='first' :
            if header[id]['from'].upper().find(filter['filter_from'].upper()) != -1:
                print id
                __run(id,post,filter)
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
        if x.find('filter_function_')!=-1 or x.find('filter_option_')!=-1:
            return True
        return False
    return filter(f,val.keys())
    pass

filter_work_word = ('del_format' , 'del_hiperlink', 'del_in_start_word', 'del_body_mail', 'set_subject',
                    'del_body_word','change_word_subject', 'send_attachments', 'no_onwer_filter')

# обрабатываем писмо по правилам
def __run(id,post,filter_work):
    key_operation=__getOperation(filter_work)
    print key_operation
    data = post.getMessage(id)
    print data
    for key in key_operation:
        if key.find('filter_function_')!=-1:
            print filter_work[key]
            if filter_work[key]=='del_hiperlink':
                data = __del_hiperlink(data)
                print data
                pass
            if filter_work[key]=='del_format':
                pass
            if filter_work[key]=='set_subject':
                pass

    pass

# удаляем ссылки
def __del_hiperlink(data):
    return re.sub(r'(http?:\/\/)?([\da-z\,-]+)\.([a-z\.]{2,6})([\/\w\.-]*)*\/?', '', data)
    pass