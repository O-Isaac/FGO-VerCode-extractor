
import os
import subprocess;
import config
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
    libil2cpp = os.path.join(config.temp_folder, "files", "lib", "armeabi-v7a", "libil2cpp.so")
    decrypt = os.path.join(config.temp_folder, "decrypt");

    print('[App] Decrypting Files!', file=sys.stdout)
    p = subprocess.Popen(f"{il2cpp} {libil2cpp} {global_metadata} {decrypt}", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True);
    p.communicate(input=b'\n')
    p.wait()