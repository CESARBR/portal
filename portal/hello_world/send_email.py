"""
Esse modulo envia emails
"""
import smtplib
import email.message

import gmail

def send_email(dest, subject, msg):
    """
    dest - destination
    subject - subject
    msg - content
    """
    server = smtplib.SMTP_SSL(gmail.URL, gmail.PORT)
    server.ehlo()
    server.login(gmail.USER, gmail.PASSWD)

    # preparing email message

    message = email.message.EmailMessage()
    message['from'] = gmail.USER
    message['to'] = dest
    message['subject'] = subject
    message.set_content(msg)
    server.send_message(message)
    server.quit()
