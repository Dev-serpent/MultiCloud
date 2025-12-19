import logging
from logging.handlers import RotatingFileHandler
from core.config import config

LOG_FILE = config.get("logging", "path", fallback="multicloud.log")

def setup_logging():
    """
    Set up the application logging.
    """
    logger = logging.getLogger("multicloud")
    logger.setLevel(logging.DEBUG)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File handler
    file_handler = RotatingFileHandler(LOG_FILE, maxBytes=1024*1024*5, backupCount=2)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

logger = setup_logging()
