import configparser
from pathlib import Path

CONFIG_FILE = Path("config.ini")

def get_config():
    """
    Get the application configuration.
    """
    config = configparser.ConfigParser()
    if CONFIG_FILE.exists():
        config.read(CONFIG_FILE)
    return config

def save_config(config):
    """
    Save the application configuration.
    """
    with open(CONFIG_FILE, "w") as f:
        config.write(f)

config = get_config()
