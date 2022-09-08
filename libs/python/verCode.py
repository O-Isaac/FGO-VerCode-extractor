import json
import os
import re
import config
import sys

from libs.python.update import get_version;

isNotVerCode = [
    "5363ad4cc05c30e0a5261c028812645a122e22ea20816678df02967c1b23bd72",
    "5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b",
    "7ae96a2b657c07106e64479eac3434e99cf0497512f58995c1396c28719501ee",
    "ffffffff00000000ffffffffffffffffbce6faada7179e84f3b9cac2fc632551",
    "ffffffff00000001000000000000000000000000fffffffffffffffffffffffc"
]

def write_verCode_data():
    stringLiteral = open(os.path.join(config.temp_folder, "decrypt", "stringliteral.json"), encoding="utf8");
    json_data = json.load(stringLiteral)

    print("[App] Writing verCode...", file=sys.stdout)

    for data in json_data:
        Value = data['value']

        if len(Value) == 64:
            
            isHash = len(re.findall("^[a-fA-F0-9]{64}$", Value)) > 0
            
            if isHash and Value.islower() and not Value in isNotVerCode:
                
                # Create JSON
                with open(os.path.join(os.getcwd(), "VerCode.json"), "w") as file:
                    version_latest = get_version()
                    
                    dataVerCode = {}
                    dataVerCode["appVer"] = version_latest;
                    dataVerCode["verCode"] = Value;

                    json.dump(dataVerCode, file)
                    return print("[App] VerCode exported succefully!", file=sys.stdout)

            
