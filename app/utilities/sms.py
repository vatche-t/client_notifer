import pickle 
from datetime import datetime
import requests
import os

from utilities import get_ips


now = datetime.utcnow()





def notif_sms():
      for ip in get_ips():
        filename = f'/root/work/client_checker_v2/app/utilities/last_beat/{ip}'
        with open(filename, 'rb')as file:
            fc = file.read()
            time_stamp = pickle.loads(fc)
        if (now - time_stamp).total_seconds() > 60 * 60:
            requests.get(f"http://ippanel.com:8080/?apikey=**********U=&pid=yym1bgzvn9t6szt&fnum=******&tnum=*****&p1=ip&v1={ip}&v2=******")
        else:
            print(f"From SMS:     client {ip} is connected....")
    
#sms  - - - -  - - - - - - - - - - - - - - - - - - - - - - -

notif_sms()

#payamtak 
