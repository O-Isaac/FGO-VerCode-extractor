import json
import os
import requests
import config
import sys 

pathRoot = os.getcwd()
pathVerCode = os.path.join(pathRoot, "VerCode.json")

def get_version():
    res = requests.get(config.url_version);
    return res.content.decode('utf8')

def check_update():
    if os.path.exists(pathVerCode):
        with open(pathVerCode) as fVerCode:
            dataVerCode = json.load(fVerCode)
            versionVerCode = dataVerCode["appVer"]
            versionAtlas = get_version() 

            if (versionVerCode != versionAtlas):
                print("Need update!", file=sys.stdout)
                return True
            else:
                print('Is not necesary update!', file=sys.stdout)
                return False
    else:
        print('First Time!', file=sys.stdout)
        return True
