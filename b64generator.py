import base64
import sys

if __name__ == '__main__':
    try:
        username = sys.argv[1]
        password = sys.argv[2]
        print("b64username={0}".format(base64.b64encode(username)))
        print("b64password={0}".format(base64.b64encode(password)))
    except Exception as e:
        print(e)
        print("command format: python3 b64generator.py <username> <password>")
