# fdu_network_auto_auth
This script is used to sign in to fudan network automaticlly

## Usage

0. Install required package

```bash
pip3 install requests
```

1. Run `install` script

```bash
cd <path to project folder>
sudo ./install
```

3. Generate base64 code of your username and password

```bash
python3 b64generator.py
```

4. Write the base64 code to `account_config.py`

   After that, the script will auto run after booting.

5. Start the service

```bash
sudo service fnaa start
sudo service fnaa status
```

6. Stop the service

```bash
sudo service fnaa stop
```
