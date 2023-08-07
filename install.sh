#!/bin/bash

if ! [ -x "$(command -v systemctl)" ]; then
  echo 'Error: systemctl does not exist. Please fix that.' >&2
  exit 1
fi

if ! [ -x "$(command -v python3)" ]; then
  echo 'Error: python3 does not exist. Please fix that.' >&2
  exit 1
fi

if ! [ -x "$(command -v pip3)" ]; then
  echo 'Error: pip3 does not exist. Please fix that.' >&2
  exit 1
fi

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit 1
fi

FILE=/etc/systemd/system/wifi-checker.service

if [[ -f "$FILE" ]]; then
    echo "File $FILE exists ! You have already installed this script, or something else is using it. Please fix that."
    exit 1
fi

FILE=/etc/Wi-Fi_Checker/main.py

if [[ -f "$FILE" ]]; then
    echo "File $FILE exists ! You have already installed this script, or something else is using it. Please fix that."
    exit 1
fi

mkdir -p /etc/systemd/system/wifi-checker
cp wifi-checker.service /etc/systemd/system/wifi-checker.service
chmod 644 /etc/systemd/system/wifi-checker.service

mkdir -p /etc/Wi-Fi_Checker/
cp main.py /etc/Wi-Fi_Checker/main.py
chmod 644 /etc/Wi-Fi_Checker/main.py

systemctl start wifi-checker
systemctl enable wifi-checker

echo "All files have been initiated."
