import os
import httpx
import config
from libs.python.logger import logger

def download_latest():
    logger.info('Creating folder...')

    os.mkdir(config.temp_folder)
    os.mkdir(os.path.join(config.temp_folder, "decrypt"))

    logger.info('Downloading latest apk...!')
    
    with httpx.stream("GET", config.url_apk, follow_redirects=True) as response:
        response.raise_for_status()

        with open(os.path.join(config.temp_folder, config.apk_name), "wb") as file:
            for chunk in response.iter_bytes():
                file.write(chunk)

    logger.info('Apk downloaded!')