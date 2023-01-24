import os
import pickle 
from datetime import datetime

from dotenv.main import load_dotenv
from pathlib import Path

import smtplib
import ssl
from email.message import EmailMessage

from utilities import get_ips

dotenv_path = Path('root/work/client_check_v2/.env')
load_dotenv(dotenv_path=dotenv_path)
last_beat = os.environ['PATH_LASTBEAT']
sender = os.environ['EMAIL_SEND']
e_pass = os.environ['EMAIL_PASS']
reciver = os.environ['EMAIL_RECIVER']

now = datetime.utcnow()



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
                em['From'] = sender
                em['To'] = reciver
                em['Subject'] = subject
                em.set_content(body)
                smtp.login(sender, e_pass)
                smtp.sendmail(sender, reciver, em.as_string())
                


def notif_email():
      for ip in get_ips():
        filename = f'{last_beat}/{ip}'
        with open(filename, 'rb')as file:
            fc = file.read()
            time_stamp = pickle.loads(fc)
        if (now - time_stamp).total_seconds() > 60 * 20:
            compose_email()
        else:
            print(f"From Email:   client {ip} is connected....")
#email  - - - -  - - - - - - - - - - - - - - - - - - - - - - -

notif_email()