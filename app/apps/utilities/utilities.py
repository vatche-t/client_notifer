import os
from datetime import datetime
def get_ips():
    results = []
    testdir = "../last_beat"
    for f in os.listdir(testdir):
        if f.endswith(''):
            results.append(f)
    return results

