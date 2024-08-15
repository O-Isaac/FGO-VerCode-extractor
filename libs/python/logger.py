import logging

logging.basicConfig(
    filemode="w", 
    filename="run.log", 
    format="%(levelname)s | %(module)s | L%(lineno)d | %(asctime)s: %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S%z",
    level=logging.INFO
)

logger = logging.getLogger("VerCode (Extractor)")