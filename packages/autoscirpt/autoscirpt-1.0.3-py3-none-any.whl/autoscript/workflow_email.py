'''
Date         : 2022-08-24 11:45:11
Author       : BDFD,bdfd2005@gmail.com
Github       : https://github.com/bdfd
LastEditTime : 2022-08-24 12:31:28
LastEditors  : BDFD
Description  : 
FilePath     : \autoscript\workflow_email.py
Copyright (c) 2022 by BDFD, All Rights Reserved. 
'''
import smtplib
import ssl
from email.message import EmailMessage

# Test email sender and receiver
# Define email sender and receiver
email_receiver = 'davidchen014@gmail.com'

# Set the subject and body of the email(Common use for all)
subject = 'Test Msg'
body = """
This is auto msg send from info email
"""

def gmail(email_receiver=email_receiver,gmail_subject=subject,gmail_body=body):
    #Sender Info
    gmail_sender = 'bdfd2005@gmail.com'
    gmail_password = 'ayuktpvvqukxfbwi'

    em = EmailMessage()
    em['From'] = gmail_sender
    em['To'] = email_receiver
    em['Subject'] = gmail_subject
    em.set_content(gmail_body)

    # Add SSL (layer of security)
    context = ssl.create_default_context()

    # Log in and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(gmail_sender, gmail_password)
        smtp.sendmail(gmail_sender, email_receiver, em.as_string())


def work_mail(email_receiver=email_receiver,workmail_subject=subject,workmail_body=body):
    #Sender Info
    workmail_sender = 'customerservice@diligentgroup.ca'
    workmail_password = 'RQG@&cLQAHS+'

    em = EmailMessage()
    em['From'] = workmail_sender
    em['To'] = email_receiver
    em['Subject'] = workmail_subject
    em.set_content(workmail_body)

    # Add SSL (layer of security)
    context = ssl.create_default_context()

    # Log in and send the email
    with smtplib.SMTP_SSL('mail.diligentgroup.ca', 465, context=context) as smtp:
        smtp.login(workmail_sender, workmail_password)
        smtp.sendmail(workmail_sender, email_receiver, em.as_string())
