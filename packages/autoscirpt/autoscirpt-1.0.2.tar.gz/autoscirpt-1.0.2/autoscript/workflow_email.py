'''
Date         : 2022-08-24 11:45:11
Author       : BDFD,bdfd2005@gmail.com
Github       : https://github.com/bdfd
LastEditTime : 2022-08-24 12:23:58
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

# Set the subject and body of the email
gmail_subject = 'Test Msg'
gmail_body = """
This is auto msg send from info email
"""

def gmail(email_receiver=email_receiver,gmail_subject=gmail_subject,gmail_body=gmail_body):
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
