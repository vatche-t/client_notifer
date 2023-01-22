# from utilities.utilities import notif_telegram as telegram
# from utilities.utilities import notife_email as email
# from utilities.utilities import notif_sms as sms

import subprocess
import time


import os
import sys
 
current = os.path.dirname(os.path.realpath(__file__))
 
parent = os.path.dirname(current)
sys.path.append(parent)

import configs

hour =  configs.CONFIGS.get('TIMEOUT')


timeout = time.time() + hour


while True: 
    process = subprocess.run(['python3', 'utilities/telegram.py'], timeout=40)
    process = subprocess.run(['python3', 'utilities/email_notif.py'], timeout=40)
    process = subprocess.run(['python3', 'utilities/sms.py'], timeout=40)
    time.sleep(300)
    if time.time() == timeout:
        break


