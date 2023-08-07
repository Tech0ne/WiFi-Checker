import sys
import os

if not os.access(sys.argv[0], os.W_OK):
    # Try to display a message
    os.system(f"zenity --info --text \"Oh, it seems that the user executing the script does not have write acces to the /etc/Wi-Fi_Checker/main.py file. This can happend if u modified the service, or if you run the script manualy. Procede to reinstall, or dont run it yourself.\"")
    sys.exit(1)

def update():
    URL = ""
