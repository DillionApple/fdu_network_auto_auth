# fdu_network_auto_auth
This script is used to sign in to fudan network automaticlly

## Usage

0. Install required package

```bash
pip3 install requests
```

1. Generate base64 code of your username and password. (base64 is not secure, it only avoids trusted people from knowing your password accidently)

```bash
python3 b64generator.py
```

Then you will get a config file called account_config.py

2. Run `install` script

```bash
cd <path to project folder>
sudo ./install
```

After that, the service should be running and will run automatically after rebooting

3. Service controls

```bash
sudo service fnaa start
sudo service fnaa status
sudo service fnaa stop
```

4. Uninstall

```bash
cd <path to project folder>
sudo ./uninstall
```
