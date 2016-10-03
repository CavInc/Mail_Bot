# -*- coding: utf-8 -*-
import os
import ConfigParser

__author__ = 'cav'

__parameters__ = {}


def LoadCFG(fname):
    config = ConfigParser.SafeConfigParser()
    config.read(fname)

    __parameters__['CONFIG'] = {'mail_mode':config.get('CONFIG','mail_mode').upper(),
                                'filter':config.get('CONFIG','filter_file'),
                                'filter_name':config.get('CONFIG','filter_name_in_single_mode')}

    __parameters__['POP'] = {'host':config.get('POP','host'),
                             'user':config.get('POP','user'),
                             'pass':config.get('POP','pass'),
                             'ssl':config.get('POP','ssl').lower(),
                             'ssl_port':config.get('POP','ssl_port').lower(),
                             'pop_port':config.get('POP','pop_port').lower()}

    __parameters__['IMAP'] = {'host':config.get('IMAP','host'),
                             'user':config.get('IMAP','user'),
                             'pass':config.get('IMAP','pass'),
                             'ssl':config.get('IMAP','ssl'),
                             'ssl_port':config.get('IMAP','ssl_port').lower(),
                             'pop_port':config.get('IMAP','imap_port').lower()}
    __parameters__['SMTP'] = {'host':config.get('SMTP','host'),
                              'user':config.get('SMTP','user'),
                              'pass':config.get('SMTP','pass'),
                              'ssl':config.get('SMTP','ssl')}
    '''
    print config.sections()
    for sec in config.sections():
        print config.options(sec)

    print __parameters__
    '''

    pass

def getPOPConfig():
    return __parameters__['POP']

def getIMAPConfig():
    return __parameters__['IMAP']

def getConfig():
    return __parameters__['CONFIG']

def getSMTP():
    return  __parameters__['SMTP']


__filters__={}

def LoadFilter(fname):
    filter = ConfigParser.SafeConfigParser()
    filter.read(fname)
    for section in filter.sections():
        row={}
        for opt in filter.options(section):
            '''
            if opt.find('filter_function_')!=-1 or opt.find('filter_option_')!=-1:
                print opt
            '''
            row[opt]=filter.get(section,opt)
            pass
        __filters__[section]=row
    return __filters__

