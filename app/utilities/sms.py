import pickle 
from datetime import datetime
import requests


import utilities as util
now = datetime.utcnow()








def notif_sms():
      for ip in util.get_ips():
        filename = f'../../last_beat/{ip}'
        with open(filename, 'rb')as file:
            fc = file.read()
            time_stamp = pickle.loads(fc)
        if (now - time_stamp).total_seconds() > 60 * 60:
            requests.get(f"http://ippanel.com:8080/?apikey=bsvLPLdjEsnYJeA43V-OAZ1oQNLOHODs_jsemvjIRPU=&pid=yym1bgzvn9t6szt&fnum=3000505&tnum=09129332760&p1=ip&v1={ip}&v2=1596")
        else:
            print(f"client {ip} is connected....")
    
#sms  - - - -  - - - - - - - - - - - - - - - - - - - - - - -