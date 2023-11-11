import logging
from colorama import init, Fore

init()

class ComposoLogHandler(logging.StreamHandler):

    def __new__(cls, *args, **kwargs):
        return super(ComposoLogHandler, cls).__new__(cls)

    def __init__(self, stream=None):
        super().__init__(stream)

    def emit(self, record):
        record.msg = f"{Fore.BLUE}Composo:{Fore.RESET} {record.msg}"
        super().emit(record)

def setup_logger():
    # Setting up logging
    logger = logging.getLogger("ComposoLogger")
    logger.setLevel(logging.DEBUG)

    # Use the custom log handler
    handler = ComposoLogHandler()
    formatter = logging.Formatter('%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger