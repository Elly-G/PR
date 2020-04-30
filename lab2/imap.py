#!/usr/bin/env python3
import imaplib
import hashlib
import getpass
import email
import email.message
import time
import os.path
import subprocess
import re
import sys

imaplib._MAXLINE = 1000000

server = 'Outlook.Office365.com'
login = "elena.gavrisco@ee.utm.md"
pause_time = 300
# >>> import hashlib
# >>> hashlib.sha1(b"qwerty").hexdigest()
pwhash = 'passwd'
password = getpass.getpass("IMAP Password: ")

if hashlib.sha1(bytearray(password, 'utf-8')).hexdigest() != pwhash:
  print("Invalid password", file = sys.stderr)
  sys.exit(1)

def main_loop_proc():
    print("Connecting to {}...".format(server))
    imap = imaplib.IMAP4_SSL(server)
    print("Connected! Logging in as {}...".format(login));
    imap.login(login, password)
    print("Logged in! Listing messages...");
    status, select_data = imap.select('ARCHIVE')
    nmessages = select_data[0].decode('utf-8')
    status, search_data = imap.search(None, 'ALL')
    for msg_id in search_data[0].split():
        msg_id_str = msg_id.decode('utf-8')
        print("Fetching message {} of {}".format(msg_id_str,
                                                 nmessages))
        status, msg_data = imap.fetch(msg_id, '(RFC822)')
        msg_raw = msg_data[0][1]
        msg = email.message_from_bytes(msg_raw,
            _class = email.message.EmailMessage)
        # mailing_list = msg.get('X-Mailing-List', 'undefined')
        mailing_list = msg.get('List-Id', 'undefined')
        mailing_list = re.sub('^(?s).*?<([^>]+?)(?:\\..*?)>.*$',
                              '\\1', mailing_list)
        timestamp = email.utils.parsedate_tz(msg['Date'])
        year, month, day, hour, minute, second = timestamp[:6]
        msg_hash = hashlib.sha256(msg_raw).hexdigest()[:16]
        fname = ("./archive/{7}/{0:04}/{0:04}-{1:02}-{2:02}/" +
                 "{0:04}-{1:02}-{2:02}-{3:02}-{4:02}-{5:02}" +
                 "-{6}.txt").format(
            year, month, day, hour, minute, second,
            msg_hash, mailing_list)
        dirname = os.path.dirname(fname)
        print("Saving message {} to file {}".format(msg_id_str, fname))
        subprocess.call('mkdir -p {}'.format(dirname), shell=True)
        with open(fname, 'wb') as f:
            f.write(msg_raw)
        imap.store(msg_id, '+FLAGS', '\\Deleted')
    imap.expunge()
    imap.logout()

while True:
    try:
        main_loop_proc()
    except Exception as e:
        print("ERROR:" + str(e))
    print("Sleeping {} seconds...".format(pause_time))
    time.sleep(pause_time)
    