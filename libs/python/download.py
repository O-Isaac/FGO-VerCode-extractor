import requests;
import config;
import os;
import sys

def download_latest():
    print('[App] Creating folder...', file=sys.stdout)
    os.mkdir(config.temp_folder);
    os.mkdir(os.path.join(config.temp_folder, "decrypt"));

    print('[App] Downloading latest apk...!', file=sys.stdout)

    # Create path to save file
    apk = os.path.join(config.temp_folder, "fate.apk")

    # Download and Save the file
    response = requests.get(config.url_apk)
    open(apk, "wb").write(response.content)

    print('[App] Apk downloaded!', file=sys.stdout)