# fdu_network_auto_auth

This script is used to sign in to fudan network automaticlly

## Requirement

It only works for Linux with python3 and pip3 installed.

You should be an sudoer of the machine.

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

This script may ask for your student id and password.

After that, the service should be installed. Run `sudo service fnaa start` to start the service.

The service will automatically start after rebooting.

2. Service controls

```bash
sudo service fnaa start
sudo service fnaa status
sudo service fnaa stop
```

3. Uninstall

```bash
cd <path to project folder>
sudo ./uninstall
```
