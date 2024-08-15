import os;

# https://fgo.square.ovh/apk/com.aniplex.fategrandorder.en.apk
url_apk = "https://fgo.bigcereal.com/apk/com.aniplex.fategrandorder.en.xapk"

# https://gplay-ver.atlasacademy.workers.dev/?id=com.aniplex.fategrandorder
url_version = "https://gplay-ver.atlasacademy.workers.dev/?id=com.aniplex.fategrandorder.en"

apk_name = url_apk.split("/")[-1]

# Temp folder
temp_folder = os.path.join(os.getcwd(), "temp")
