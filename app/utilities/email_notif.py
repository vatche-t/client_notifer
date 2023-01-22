
import pickle 
from datetime import datetime

import sys
sys.path.insert(0,'../..')
import configs


import smtplib
import ssl
from email.message import EmailMessage

import utilities as util
now = datetime.utcnow()


#email  - - - -  - - - - - - - - - - - - - - - - - - - - - - -
def compose_email():
     context = ssl.create_default_context()
     for ip in util.get_ips():
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
      for ip in util.get_ips():
        filename = f'../../last_beat/{ip}'
        with open(filename, 'rb')as file:
            fc = file.read()
            time_stamp = pickle.loads(fc)
        if (now - time_stamp).total_seconds() > 60 * 20:
            compose_email()
        else:
            print(f"client {ip} is connected....")
#email  - - - -  - - - - - - - - - - - - - - - - - - - - - - -

notif_email()