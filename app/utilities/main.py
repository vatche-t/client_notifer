# from utilities.utilities import notif_telegram as telegram
# from utilities.utilities import notife_email as email
# from utilities.utilities import notif_sms as sms

import subprocess
import time


import os, sys
sys.path.append("../../")
import configs



timeout = time.time() + configs.CONFIGS.get('TIMEOUT')


while True: 
    process = subprocess.run(['python3', 'telegram.py'], timeout=40)
    process = subprocess.run(['python3', 'email_notif.py'], timeout=40)
    process = subprocess.run(['python3', 'sms.py'], timeout=40)
    time.sleep(300)
    if time.time() == timeout:
        break


