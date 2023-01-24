import os
from datetime import datetime
def get_ips():
    results = []
    testdir = "/root/work/client_checker_v2/app/utilities/last_beat"
    for f in os.listdir(testdir):
        if f.endswith(''):
            results.append(f)
    return results


for ip in get_ips():
    print(ip)
    
