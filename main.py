import os
import requests;
import subprocess;
import shutil;
import json;

from pyaxmlparser import APK;
from version import get_version;

pathRoot = os.getcwd()
pathVerCode = os.path.join(pathRoot, "VerCode.json")
pathAPK = os.path.join(pathRoot, "temp", "fate.apk")

def download_apk(region):
    print("Downloading APK...")
    
    if(region == "na"):
        response = requests.get("https://fgo.square.ovh/apk/com.aniplex.fategrandorder.en.apk")
        open("temp/fate.apk", "wb").write(response.content)

    if(region == "jp"):
        response = requests.get("https://fgo.square.ovh/apk/com.aniplex.fategrandorder.apk")
        open("temp/fate.apk", "wb").write(response.content)

    print("Apk donwloaded and builded!")

def create_temporal_folder():
    tempFolderPath = os.path.join(pathRoot, "temp")
    os.mkdir(tempFolderPath)
    print("Temporal folder created!")

def decompiling_apk():
    cppTwoIL = os.path.join(pathRoot, "cpp2il.exe")
    subprocess.run([cppTwoIL, "--game-path", "./temp/fate.apk", "--output-root", "./temp/dlls", "--just-give-me-dlls-asap-dammit"])    

def get_verCode_from_dlls():
    extractor = os.path.join(pathRoot, "extractor", "verCode.exe")
    Assembly_CSharp = os.path.join(pathRoot, "temp", "dlls", "Assembly-CSharp.dll")
    subprocess.run([extractor, Assembly_CSharp])


def remove_temp_directory():
    print("Trying remove temp dir")
    
    try:
        tempPath = os.path.join(pathRoot, "temp")
        shutil.rmtree(tempPath)
        print("Temp directory removed!")
    except:
        print("Error on remove directory")


def check_app_version_on_extract():
    apk = APK(pathAPK)

    with open(pathVerCode, "r") as f:
        data = json.load(f)
        
        if (data['appVer'] == "Unknow"):
            with open(pathVerCode, "w") as fw:
                new_verCode = {
                    "appVer": apk.version_name,
                    "verCode": data["verCode"]
                }
                json.dump(new_verCode, fw)


def extract_verCode():
    create_temporal_folder()
    download_apk("jp") # Change depends of the region
    decompiling_apk()
    get_verCode_from_dlls()


def check_update():
    with open(pathVerCode) as fVerCode:
        dataVerCode = json.load(fVerCode)
        versionVerCode = dataVerCode["appVer"]
        versionAtlas = get_version("JP") # Change depends of the region in uppercase
        
     

        if (versionVerCode != versionAtlas):
            print("Need update!")
            extract_verCode()
            check_app_version_on_extract()
            remove_temp_directory()
        else:
            print('Is not necesary update!')



if __name__ == '__main__':
    check_update()