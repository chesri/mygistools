#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      chrism
#
# Created:     02/03/2018
# Copyright:   (c) chrism 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------


# Import smtplib for the actual sending function
import os, sys, smtplib,mimetypes
import time

from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# Here are the email package modules we'll need
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

COMMASPACE = ', '

# Create the container (outer) email message.
outer = MIMEMultipart()
outer['Subject'] = 'Our family reunion'
me = 'banian92174@mypacks.net'
#target = ['headofschool1712@gmail.com',]
target = ['lope21665@mypacks.net']
outer['From'] = me
outer['To'] = COMMASPACE.join(target)
outer.preamble = 'Test Python Email'

lists_of_files = [r'C:\Users\chrism\Pictures\Capture.PNG',]
filename = 'iTuneCard.png'

# Assume we know that the image files are all in PNG format
for file in lists_of_files:
    ctype, encoding = mimetypes.guess_type(file)
    maintype, subtype = ctype.split('/', 1)

    fp = open(file, 'rb')
    msg = MIMEBase(maintype, subtype)
    msg.set_payload(fp.read())
    fp.close()
    # Encode the payload using Base64
    encoders.encode_base64(msg)
msg.add_header('Content-Disposition', 'attachment', filename=filename)
outer.attach(msg)

# Send the email via our own SMTP server.

for i in range(0,1):
    s = smtplib.SMTP(host='smtpauth.earthlink.net', port=587)
    s.login('chris.mcguire@earthlink.net', 'mcg2kids')
    s.sendmail(me, target, outer.as_string())
    s.quit()
    print "sleeping..."
    wait = 60 * 5   # seconds times minutes
    time.sleep(wait)
s.quit()