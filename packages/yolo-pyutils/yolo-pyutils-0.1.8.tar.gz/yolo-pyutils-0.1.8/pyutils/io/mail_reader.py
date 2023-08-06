import logging
from imapclient import IMAPClient


class MailReader:

    def __init__(self, imap_host, imap_port, user, pwd, charset='UTF-8', ssl=True):
        self.__imap_host = imap_host
        self.__imap_port = imap_port
        self.__user = user
        self.__pwd = pwd
        self.__client = None
        self.__charset = charset
        self.__ssl = ssl

    def start(self):
        self.__client = IMAPClient(self.__imap_host, ssl=self.__ssl, port=self.__imap_port)
        self.__client.login(self.__user, self.__pwd)

    def stop(self):
        self.__client.logout()

    def search_inbox(self, criteria, search_key_alias):
        self.__client.select_folder('INBOX')
        messages = self.__client.search(criteria=criteria, charset=self.__charset)
        logging.info("%d messages found by criteria={}".format(len(messages), criteria))
        mails = list()
        if len(messages) > 0:
            for mail_id, data in self.__client.fetch(messages, search_key_alias.keys()).items():
                mail = dict()
                for key, alias in search_key_alias.items():
                    mail[alias] = data[bytes(key, self.__charset)].decode(self.__charset)
                mails.append(mail)
        return mails
