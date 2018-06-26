import base64
import sys

if __name__ == '__main__':
    try:
        username = sys.argv[1]
        password = sys.argv[2]
        username = username.encode("utf8")
        password = password.encode("utf8")
        print("b64username={0}".format(base64.b64encode(username)))
        print("b64password={0}".format(base64.b64encode(password)))
        with open("account_config.py", "w") as f:
            f.write("b64username={0}\n".format(base64.b64encode(username)))
            f.write("b64password={0}".format(base64.b64encode(password)))
            f.close()
    except Exception as e:
        print(e)
        print("command format: python3 b64generator.py <username> <password>")
