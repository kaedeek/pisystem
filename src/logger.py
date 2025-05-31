from logging import getLogger, Formatter
from colorama import Fore, Style, init
import logging

init()

COLORS = {
    'DEBUG': Fore.BLUE,
    'INFO': Fore.GREEN,
    'WARNING': Fore.YELLOW,
    'ERROR': Fore.RED,
    'CRITICAL': Fore.RED + Style.BRIGHT
}

class ColoredFormatter(Formatter):
    def format(self, record):
        message = super().format(record)
        color = COLORS.get(record.levelname, Fore.WHITE)
        return f"{color}{message}{Style.RESET_ALL}"

logger = getLogger('colored_logger')
formatter = ColoredFormatter('[%(levelname)s] %(asctime)s : %(message)s')

handler = logging.StreamHandler()
handler.setFormatter(formatter)

logger.handlers = []
logger.addHandler(handler)
logger.setLevel(logging.INFO)

def debug(msg, *args, **kwargs):
    logger.debug(msg, *args, **kwargs)

def info(msg, *args, **kwargs):
    logger.info(msg, *args, **kwargs)

def warning(msg, *args, **kwargs):
    logger.warning(msg, *args, **kwargs)

def error(msg, *args, **kwargs):
    logger.error(msg, *args, **kwargs)

def critical(msg, *args, **kwargs):
    logger.critical(msg, *args, **kwargs)