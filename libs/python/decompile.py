
import os
import subprocess;
import config

from libs.python.logger import logger

# java -jar .\apktool.jar d .\fate.apk --output '.\temp\' -f
def decompile_apk():
    apktool = os.path.join(os.getcwd(), "libs", "java", "apktool.jar")
    apkeditor = os.path.join(os.getcwd(), "libs", "java", "apkeditor.jar")
    apk = os.path.join(config.temp_folder, config.apk_name)

    if config.apk_name.endswith("xapk"):
        logger.info("XAPK detected. Merging into APK files.")
        result = subprocess.run(["java", "-jar", apkeditor, "m", "-i", apk, "-o", apk.replace("xapk", "apk")],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )

        # All data is sterr maybe is a error of apkeditor is reported
        for line in result.stderr.splitlines():
            if line.strip():
                logger.info(line)

        apk = apk.replace("xapk", "apk")
    
    logger.info("Decompiling apk...")

    result = subprocess.run(["java", "-jar", apktool, "d", apk, "--output", "./temp/files/", "-f"],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )

    for line in result.stdout.splitlines():
            if line.strip():
                logger.info(line)

    logger.info("Decompile apk succesfully!")


def decrypt():
    il2cpp = os.path.join(os.getcwd(), "libs", "Il2CppDumper", "Il2CppDumper.exe")
    global_metadata = os.path.join(config.temp_folder, "files", "assets", "bin", "Data", "Managed", "Metadata", "global-metadata.dat")
    decrypt = os.path.join(config.temp_folder, "decrypt");

    logger.info("Getting available libraries directories from apk")
    lib_dir_path = os.path.join(config.temp_folder, "files", "lib")
    lib_folders = os.listdir(lib_dir_path)

    logger.info(f"ArchLibs avalibles {lib_folders}")
    logger.info(f"Getting libil2cpp from {lib_folders[0]}")
    lib_dir_name = lib_folders[0]
    libil2cpp = os.path.join(config.temp_folder, "files", "lib", lib_dir_name, "libil2cpp.so")

    logger.info('Decrypting Files!')
    result = subprocess.run(
        [il2cpp, libil2cpp, global_metadata, decrypt],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )

    for line in result.stdout.splitlines():
        if line.strip():
            logger.info(line)