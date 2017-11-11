import time
import datetime
import random

import requests

from account_config import *

url = r'http://10.108.255.249/include/auth_action.php'

payload = {
    'action': 'login',
    'username': username,
    'password': password,
    'ac_id': 1,
    'ajax': 1,
}

random.seed(time.time())

while True:

    response = requests.post(url, data=payload)

    datetime_now = datetime.datetime.now()

    print("{time}: {response}".format(time=datetime_now, response=response.content.decode('utf-8')))
        
    # sleep from 10 mins to 60 mins
    sleep_seconds = random.randrange(600, 3600)
    interval = datetime.timedelta(seconds=sleep_seconds)    
    print("Next request will at {time} in {seconds} seconds".format(time=datetime_now+interval, seconds=sleep_seconds))

    time.sleep(sleep_seconds)
