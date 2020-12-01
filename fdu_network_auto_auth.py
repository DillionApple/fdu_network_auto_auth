import time
import datetime
import random
import threading
import base64
import os

import requests

from account_config import *

url = r'http://10.108.255.249/include/auth_action.php'

random.seed(time.time())

def do_login():

    print("Do Login")
    # print('username: ' + base64.b64decode(b64username))
    # print('password: ' + base64.b64decode(b64password))

    get_user_ip_cmd = """
    ifconfig | grep "inet" | grep "\d*\.\d*\.\d*\.\d*" | grep -v "127.0.0.1" |  awk '{ print $2 }'
    """

    user_ip = os.popen(get_user_ip_cmd).read().strip()
    print("Your IP address is {0}".format(user_ip))

    payload = {
        'action': 'login',
        'username': base64.b64decode(b64username),
        'password': base64.b64decode(b64password),
        'ac_id': 1,
        'user_ip': user_ip,
        'nas_ip': '',
        'user_mac': '',
        'save_me': 0,
        'ajax': 1,
    }
    
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

def test_network():
    retry_times = 3
    for i in range(retry_times):
        ret_code = os.system("ping www.baidu.com -c 1 -W 1")
        if ret_code == 0:
            log("Ping success")
            return True
    log("Ping failed after {0} times".format(retry_times))
    return False

def log(msg):
    print("{time}: {msg}".format(time=datetime.datetime.now(), msg=msg))

def start_making_request():

    while True:
        if (not test_network()):
            log("Network connection is bad, try to relogin")
            do_logout()
            if do_login():
                log("Login success")
            else:
                log("Login fail")
        
        # sleep 1 minute
        sleep_seconds = 60
        time.sleep(sleep_seconds)

if __name__ == '__main__':
    threading.Thread(target=start_making_request).start()
