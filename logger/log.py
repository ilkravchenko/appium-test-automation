from datetime import datetime
import logging
import os
import time
from colorama import init, Fore

init(autoreset=True)


class ColoredFormatter(logging.Formatter):
    LOG_COLORS = {
        logging.DEBUG: Fore.CYAN,
        logging.INFO: Fore.GREEN,
        logging.WARNING: Fore.YELLOW,
        logging.ERROR: Fore.LIGHTRED_EX,
        logging.CRITICAL: Fore.RED,
    }

    def format(self, record):
        log_message = super().format(record)
        return f"{self.LOG_COLORS.get(record.levelno, '')}{log_message}"


class Logging:

    def __init__(self, log_file=f"logs/app_{datetime.today().strftime('%d_%B_%Y_%H_%M_%S')}.log"):
        # Ensure the logs folder exists
        os.makedirs(os.path.dirname(log_file), exist_ok=True)

        # Configure logging settings with the colored formatter
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s - %(levelname)s - %(message)s',
                            handlers=[
                                logging.FileHandler(log_file),
                                logging.StreamHandler()
                            ])

        # Add the colored formatter to the handlers
        for handler in logging.getLogger().handlers:
            handler.setFormatter(ColoredFormatter(fmt=handler.formatter._fmt, datefmt=handler.formatter.datefmt))

    def wait_for_seconds(self, seconds_to_wait=5):
        """Hard sleep if absolutely needed. Defaults to 5 seconds"""
        logging.debug(msg=f'Waiting for {seconds_to_wait} seconds...')
        time.sleep(seconds_to_wait)

    def final_logger(self, element):
        """logging output for the final clause debug"""
        logging.info(msg=f'Element found: {bool(element)}')

    def element_logger(self, find_by, identifier: str, element):
        """logging output for the element debug"""
        logging.info(msg=f'Using {find_by} to find identifier {identifier}')

    def logging_debug(self, message):
        logging.debug(msg=message)

    def logging_info(self, message):
        logging.info(msg=message)

    def logging_error(self, message):
        logging.error(msg=message)
