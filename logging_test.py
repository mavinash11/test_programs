import logging


logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")
console_handler = logging.StreamHandler()
logger.addHandler(console_handler)
formatter = logging.Formatter("{asctime}-{levelname}:{filename}: {message}", style="{", datefmt="%Y-%m-%d %H:%M:%S")
console_handler.setFormatter(formatter)
# logging.info("Test Message")


def print_test():
    logger.info("Test Message New")
    pass

print_test()