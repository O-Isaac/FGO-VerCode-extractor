
import os
import subprocess;
import config
import sys;

# java -jar .\apktool.jar d .\fate.apk --output '.\temp\' -f
def decompile_apk():
    apktool = os.path.join(os.getcwd(), "libs", "java", "apktool.jar")
    apkeditor = os.path.join(os.getcwd(), "libs", "java", "apkeditor.jar")
    apk = os.path.join(config.temp_folder, config.apk_name)

    if config.apk_name.endswith("xapk"):
        print("[App]", "Detected xapk change decompile method to merge & decompile.")
        subprocess.run(["java", "-jar", apkeditor, "m", "-i", apk, "-o", apk.replace("xapk", "apk")])
        apk = apk.replace("xapk", "apk")
    
    print('[App] Decompiling apk...')
    subprocess.run(["java", "-jar", apktool, "d", apk, "--output", "./temp/files/", "-f"])


def decrypt():
    il2cpp = os.path.join(os.getcwd(), "libs", "Il2CppDumper", "Il2CppDumper.exe")
    global_metadata = os.path.join(config.temp_folder, "files", "assets", "bin", "Data", "Managed", "Metadata", "global-metadata.dat")
    decrypt = os.path.join(config.temp_folder, "decrypt");

    print("[App] Getting available libraries directories from apk")
    lib_dir_path = os.path.join(config.temp_folder, "files", "lib")
    lib_folders = os.listdir(lib_dir_path)

    print(f"[App] ArchLibs avalibles {lib_folders}")
    print(f"[App] Getting libil2cpp from {lib_folders[0]}")
    lib_dir_name = lib_folders[0]
    libil2cpp = os.path.join(config.temp_folder, "files", "lib", lib_dir_name, "libil2cpp.so")

    print('[App] Decrypting Files!')
    subprocess.run([il2cpp, libil2cpp, global_metadata, decrypt])