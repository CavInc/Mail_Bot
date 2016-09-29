#-*- coding: utf-8 -*-
import quopri
import base64
import re
import  email,poplib,imaplib
from email.header import decode_header

__author__ = 'cav'
#https://pymotw.com/2/imaplib/

POST_MODE_POP = 0
POST_MODE_IMAP = 1

class POST_EMAIL:
    mask = {'windows-1251':'cp1251','koi8-r':'koi8-r',None:'utf-8','utf-8':'utf-8'}
    head_mail = {}
    mode = None

    imap_mailbox=()

    def __init__(self,server,user,password,mode=POST_MODE_POP,ssl_mode=None,pop_port='default'):
        self.mode = mode
        if mode == POST_MODE_POP:
            if ssl_mode == None:
                self.mp = poplib.POP3(server)
            else :
                self.mp = poplib.POP3_SSL(server)
            print self.mp.getwelcome()

            self.mp.user(user)
            self.mp.pass_(password)
            self.response,self.lst,self.octet = self.mp.list()

        if mode == POST_MODE_IMAP:
            if ssl_mode == None:
                self.mp = imaplib.IMAP4(server)
            else :
                self.mp = imaplib.IMAP4_SSL(server)

            self.mp.login(user,password)

            self.result,data= self.mp.list()
            print self.result,data
            for line in data:
                flags, delimiter, mailbox_name = self.parse_list_response(line)
                print flags
                #print delimiter
                print mailbox_name
                print email.Header.decode_header(mailbox_name)
                if mailbox_name[:1]=='&':
                    print mailbox_name

                print self.mp.status(mailbox_name,'(MESSAGES RECENT UIDNEXT UIDVALIDITY UNSEEN)')

            self.mp.select()

            self.result,self.ids = self.mp.search(None, 'ALL')
            pass

        pass

    def quit(self):
        if self.mode== POST_MODE_POP:
            self.mp.quit()
        else :
            self.mp.logout()



    list_response_pattern = re.compile(r'\((?P<flags>.*?)\) "(?P<delimiter>.*)" (?P<name>.*)')
    def parse_list_response(self,line):
        flags, delimiter, mailbox_name = self.list_response_pattern.match(line).groups()
        mailbox_name = mailbox_name.strip('"')
        return (flags, delimiter, mailbox_name)

    def getHeader(self):
        if self.mode == POST_MODE_POP:
            for msgnum,msgsize in [i.split() for i in self.lst]:
                (resp,lines,octet) = self.mp.top(msgnum,0)
                msgtxt= "\n".join(lines)+"\n\n"
                msg=email.message_from_string(msgtxt)
                value , charset =  decode_header(msg['Subject'])[0]
                value = value.decode(self.mask[charset]).encode('utf-8')
                resipient = msg['From']
                self.head_mail[msgnum]= {'from':resipient,'subject':value}

        if self.mode == POST_MODE_IMAP:
            for id in self.ids[0].split():
                result,resipient = self.mp.fetch(id,'(BODY.PEEK[HEADER.FIELDS (FROM)])')
                resipient = email.Header.decode_header(resipient[0][1].strip()[6:]).pop()

                subject =  self.mp.fetch(id,'(BODY.PEEK[HEADER.FIELDS (SUBJECT)])')[1][0][1].strip()[9:]
                subject = email.Header.decode_header(subject)
                subject = subject[0][0].decode(subject[0][1]) if subject[0][1] else subject[0][0]
                self.head_mail[id] = {'from':resipient[0],'subject': subject}
                pass
        return self.head_mail
    pass

    '''
      возвращаем тело письма
    '''
    def getMessage(self,num_message):
        msg=''
        if self.mode == POST_MODE_POP:
            msg = email.message_from_string('\n'.join(self.mp.retr(num_message)[1]))
            pass
        if self.mode == POST_MODE_IMAP:
            typ, msg = self.mp.fetch(num_message, '(RFC822)')
            msg=msg[0][1]
            pass
        return msg
        pass

    '''
      удаляем писмо на сервере
    '''
    def delMessage(selfs,num_message):
        pass




