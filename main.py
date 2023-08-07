from datetime import datetime

import subprocess
import requests

import time
import sys
import os


SSID = ""
SERVER_URL = "https://wifi-checker.piasco.repl.co"

def log(*args, start='[-] ', sep=' ', end='\n'):
    date = datetime.now().strftime("{%d/%m/%Y %H:%M:%S} ")
    print(f"{start}{date}{sep.join(args)}", end=end)

def debug(*args):
    log(start="[ ] \033[90m", end="\033[0m\n", *args)

def info(*args):
    log(start="[+] \033[36m", end="\033[0m\n", *args)

def good(*args):
    log(start="[+] \033[92m", end="\033[0m\n", *args)

def warn(*args):
    log(start="[!] \033[91m", end="\033[0m\n", *args)

def error(*args):
    log(start="/!\\ \033[41m", end="\033[0m\n", *args)

def fatal(*args, code=1):
    error(*args)
    sys.exit(code)

if not os.access(sys.argv[0], os.W_OK):
    # Try to display a message
    os.system(f"zenity --info --text \"Oh, it seems that the user executing the script does not have write acces to the /etc/Wi-Fi_Checker/main.py file. This can happend if u modified the service, or if you run the script manualy. Procede to reinstall, or dont run it yourself.\"")
    sys.exit(1)

def update():
    with open(sys.argv[0], 'rb') as f:
        data = f.read()
    URL = "https://raw.githubusercontent.com/Tech0ne/WiFi-Checker/main/main.py"
    r = requests.get(URL)
    if r.content == data:
        return False
    with open(sys.argv[0], 'wb+') as f:
        f.write(r.content)
    return True

def main():
    info("Updating...")
    if update():
        warn("New version found !")
        info("Please restart !")
        sys.exit(0)
    debug("Already up to date")
    while 1:
        mac = subprocess.check_output(["iwgetid", "-a"]).decode().split(' ')[-1]
        if mac.upper() != SSID.upper():
            time.sleep(3600)
            continue
        r = requests.get("https://google.com")
        tm = r.elapsed.total_seconds()
        info(f"Current ping to google is {tm}")
        requests.post(SERVER_URL + "/update", data = {'ping': tm})
        time.sleep(9 * 60)
