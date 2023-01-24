import os
import pickle 
from datetime import datetime
import requests

from dotenv.main import load_dotenv
from pathlib import Path

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) #
CONFIG_PATH = os.path.join(ROOT_DIR, '.env')


dotenv_path = Path('CONFIG_PATH')
load_dotenv(dotenv_path=dotenv_path)
last_beat = os.environ['PATH_LASTBEAT']

from utilities import get_ips
now = datetime.utcnow()



#telegram  - - - -  - - - - - - - - - - - - - - - - - - - - - - -
def send_to_telegram(message):

    apiToken = os.environ['API_TOKEN']
    chatID = os.environ['CHAT_ID']
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)
        

def notif_telegram():
    for ip in get_ips():
         filename = f"{last_beat}/{ip}"
         with open(filename, 'rb')as file:
            fc = file.read()
            time_stamp = pickle.loads(fc)
         if (now - time_stamp).total_seconds() > 60 * 5:
            send_to_telegram(f"Client {ip} has been disconnected for more than {now - time_stamp} minutes at: {now}")
         else:
               print(f"From Telegram:   client {ip} is connected....")
#telegram  - - - -  - - - - - - - - - - - - - - - - - - - - - - -

notif_telegram()