import os
import subprocess
import time

hour = 60*120

timeout = time.time() + hour


while True: 
    process = subprocess.run(['python3', 'app/utilities/telegram.py'], timeout=40)
    process = subprocess.run(['python3', 'app/utilities/email_notif.py'], timeout=40)
    process = subprocess.run(['python3', 'app/utilities/sms.py'], timeout=40)
    time.sleep(300)
    if time.time() == timeout:
        break


