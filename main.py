from libs.python.update import check_update
from libs.python.download import download_latest
from libs.python.decompile import decompile_apk, decrypt
from libs.python.verCode import write_verCode_data

import sys

if check_update():
    download_latest()
    decompile_apk()
    decrypt()
    write_verCode_data();
else:
    print('[App] Workflow Canceled!', file=sys.stdout)