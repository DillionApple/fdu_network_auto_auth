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

2. Write the base64 code to `account_config.py`

3. Run `install` script

```bash
cd <path to project folder>
sudo ./install
```

After that, the service should be running and will run automatically after rebooting

4. Service controls

```bash
sudo service fnaa start
sudo service fnaa status
sudo service fnaa stop
```

5. Uninstall

```bash
cd <path to project folder>
sudo ./uninstall
```
