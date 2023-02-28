
import os;
import subprocess;
import config;
import sys;

def decompile_apk():
    apktool = os.path.join(os.getcwd(), "libs", "java", "apktool.jar")
    apk = os.path.join(config.temp_folder, "fate.apk")

    #java -jar .\apktool.jar d .\fate.apk --output '.\temp\' -f
    print('[App] Decompiling apk...', file=sys.stdout)
    subprocess.run(f"java -jar {apktool} d {apk} --output ./temp/files/ -f")

def decrypt():
    il2cpp = os.path.join(os.getcwd(), "libs", "Il2CppDumper", "Il2CppDumper-x86.exe")
    global_metadata = os.path.join(config.temp_folder, "files", "assets", "bin", "Data", "Managed", "Metadata", "global-metadata.dat")
    decrypt = os.path.join(config.temp_folder, "decrypt");

    print("[App] Getting available libraries directories from apk")
    lib_folders = os.listdir(config.temp_folder, "files", "lib")

    print(f"[App] ArchLibs avalibles {lib_folders}")
    print(f"[App] Getting libil2cpp from {lib_folders[0]}")
    lib_dir_name = lib_folders[0]
    libil2cpp = os.path.join(config.temp_folder, "files", "lib", lib_dir_name, "libil2cpp.so")

    print('[App] Decrypting Files!', file=sys.stdout)
    p = subprocess.Popen(f"{il2cpp} {libil2cpp} {global_metadata} {decrypt}", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True);
    p.communicate(input=b'\n')
    p.wait()