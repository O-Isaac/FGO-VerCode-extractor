import json
import os
import config
import httpx

from libs.python.logger import logger

pathRoot = os.getcwd()
pathVerCode = os.path.join(pathRoot, "VerCode.json")

def get_version():
    return httpx.get(config.url_version).text        

def is_necesary_update(current, latest):
    return current != latest

def check_update():
    if os.path.exists(pathVerCode):
        with open(pathVerCode) as fVerCode:
            dataVerCode = json.load(fVerCode)
            versionVerCode = dataVerCode["appVer"]
            versionAtlas = get_version() 
            logger.info(f"Current installed version: {versionVerCode}, up-to-date with the latest available version: {versionAtlas}.")
            return is_necesary_update(versionVerCode, versionAtlas)
    else:
        
        return True
