import time
import datetime
import random
import threading

import requests

from account_config import *

url = r'http://10.108.255.249/include/auth_action.php'

random.seed(time.time())

def do_login():

    print("Do Login")

    payload = {
        'action': 'login',
        'username': username,
        'password': password,
        'ac_id': 1,
        'ajax': 1 }
    
    response = requests.post(url, data=payload)
    response_str = response.content.decode('utf-8')

    if (response_str.find("login_ok") == -1):
        return False
    return True

def do_logout():

    print("Do Logout")

    payload = {
        'action': 'logout',
        'username': '',
        'ajax': 1}
    
    response = requests.post(url, data=payload)

def start_making_request():

    while True:
        datetime_now = datetime.datetime.now()
        if do_login():
            print("{time}: Login Success".format(time=datetime_now))
        else:
            do_logout()
            if do_login():
                print("{time}: Login Success".format(time=datetime_now))
            else:                
                print("{time}: Login Fail".format(time=datetime_now))
        
        # sleep from 10 mins to 60 mins
        sleep_seconds = random.randrange(600, 3600)
        interval = datetime.timedelta(seconds=sleep_seconds)    
        print("Next request will at {time} in {seconds} seconds".format(time=datetime_now+interval, seconds=sleep_seconds))

        time.sleep(sleep_seconds)

if __name__ == '__main__':
    threading.Thread(target=start_making_request).start()
