import pickle 
import os
from datetime import datetime
import requests

import sys
sys.path.insert(0,'../..')
import configs

import smtplib
import ssl
from email.message import EmailMessage




now = datetime.utcnow()

def get_ips():
    results = []
    testdir = "../../last_beat"
    for f in os.listdir(testdir):
        if f.endswith(''):
            results.append(f)
    return results



#telegram  - - - -  - - - - - - - - - - - - - - - - - - - - - - -
def send_to_telegram(message):

    apiToken = configs.CONFIGS.get('API_TOKEN')
    chatID = configs.CONFIGS.get('CHAT_ID')
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)
        

def notif_telegram():
    for ip in get_ips():
         filename = f'../../last_beat/{ip}'
         with open(filename, 'rb')as file:
            fc = file.read()
            time_stamp = pickle.loads(fc)
         if (now - time_stamp).total_seconds() > 60 * 5:
            send_to_telegram(f"Client {ip} has been disconnected for more than 5 minutes at: {now}")
         else:
               send_to_telegram(f"client {ip} is connected....")
#telegram  - - - -  - - - - - - - - - - - - - - - - - - - - - - -


#email  - - - -  - - - - - - - - - - - - - - - - - - - - - - -

def compose_email():
     context = ssl.create_default_context()
     for ip in get_ips():
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                                        
                subject = 'Client has been disconnected for to long!!'
                body = f"""
                'Client {ip} has been disconnected for more than 20 minutes at: {now}'
                """
                em = EmailMessage()
                em['From'] = configs.CONFIGS.get('e_sender')
                em['To'] = configs.CONFIGS.get('e_reciver')
                em['Subject'] = subject
                em.set_content(body)
                smtp.login(configs.CONFIGS.get('e_sender'), configs.CONFIGS.get('e_pass'))
                smtp.sendmail(configs.CONFIGS.get('e_sender'), configs.CONFIGS.get('e_reciver'), em.as_string())


def notif_email():
      for ip in get_ips():
        filename = f'../../last_beat/{ip}'
        with open(filename, 'rb')as file:
            fc = file.read()
            time_stamp = pickle.loads(fc)
        if (now - time_stamp).total_seconds() > 60 * 20:
            compose_email()
        else:
            print(f"client {ip} is connected....")
#email  - - - -  - - - - - - - - - - - - - - - - - - - - - - -

#sms  - - - -  - - - - - - - - - - - - - - - - - - - - - - -

def notif_sms():
      for ip in get_ips():
        filename = f'../../last_beat/{ip}'
        with open(filename, 'rb')as file:
            fc = file.read()
            time_stamp = pickle.loads(fc)
        if (now - time_stamp).total_seconds() > 60 * 60:
            requests.get(f"http://ippanel.com:8080/?apikey=bsvLPLdjEsnYJeA43V-OAZ1oQNLOHODs_jsemvjIRPU=&pid=yym1bgzvn9t6szt&fnum=3000505&tnum=09129332760&p1=ip&v1={ip}&v2=1596")
        else:
            print(f"client {ip} is connected....")
    
#sms  - - - -  - - - - - - - - - - - - - - - - - - - - - - -


notif_telegram()
notif_email()
notif_sms()
