import logging

logging.basicConfig(
    filemode="w", 
    filename="run.log", 
    format="%(levelname)s | %(module)s | L%(lineno)d | %(asctime)s: %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S%z",
    level=logging.INFO
)

logger = logging.getLogger("VerCode (Extractor)")

def log_subprocess(result):
    if result.stdout:
        for line in result.stdout.splitlines():
            logger.info(line)
    
    if result.stderr:
        for line in result.stderr.splitlines():
            logger.error(line)