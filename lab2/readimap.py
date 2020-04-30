#!/usr/bin/env python3
import imaplib
import base64
import os
import email

email_user = input('Email: ')
email_pass = input('Password: ')

mail = imaplib.IMAP4_SSL("Outlook.Office365.com", 993)

mail.login(email_user, email_pass)

mail.select('Archive')

type, data = mail.search(None, 'ALL')
mail_ids = data[0]
id_list = mail_ids.split()

for num in data[0].split():
    typ, data = mail.fetch(num, '(RFC822)' )
    raw_email = data[0][1]
# converts byte literal to string removing b''
    raw_email_string = raw_email.decode('utf-8')
    email_message = email.message_from_string(raw_email_string)
# downloading attachments
    for part in email_message.walk():
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue
        fileName = part.get_filename()    

        if bool(fileName):
            filePath = os.path.join('/home/lenag/Desktop/anul 3 sem1/anul 3 sem 2/PR/lab2/', fileName)

            if not os.path.isfile(filePath) :
                fp = open(filePath, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()
        subject = str(email_message).split("Subject: ", 1)[1].split("\nTo:", 1)[0]
        # print("Downloaded '{fileName}' from email titled '{subject}'.".format(fileName=fileName, subject=subject))
        for response_part in data:
            if isinstance(response_part, tuple):
                msg = email.message_from_string(response_part[1].decode('utf-8'))
                email_subject = msg['subject']
                email_to = msg['to']
                email_from = msg['from']
                print ('From : ' + email_from + '\n')
                print ('To : ' + email_to + '\n')
                print(msg.get_payload(decode=True))
