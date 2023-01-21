# from utilities.utilities import notif_telegram as telegram
# from utilities.utilities import notife_email as email
# from utilities.utilities import notif_sms as sms

import subprocess
import time

while True: 
    process = subprocess.run(['python3', 'utilities.py'], timeout=40)
    time.sleep(300)


