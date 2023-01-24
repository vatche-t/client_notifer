import os
import pickle 
from datetime import datetime
import requests
import sys
sys.path.append('/root/work/client_checker_v2')
import configs



from utilities import get_ips
now = datetime.utcnow()



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
         filename = f'/root/work/client_checker_v2/app/utilities/last_beat/{ip}'
         with open(filename, 'rb')as file:
            fc = file.read()
            time_stamp = pickle.loads(fc)
         if (now - time_stamp).total_seconds() > 60 * 5:
            send_to_telegram(f"Client {ip} has been disconnected for more than {now - time_stamp} minutes at: {now}")
         else:
               print(f"From Telegram:   client {ip} is connected....")
#telegram  - - - -  - - - - - - - - - - - - - - - - - - - - - - -

notif_telegram()