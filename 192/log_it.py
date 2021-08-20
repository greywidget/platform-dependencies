import logging
from typing import Callable

LOGGER = "pybites_logger"
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(LOGGER)

DEBUG = log.debug
INFO = log.info
WARNING = log.warning
ERROR = log.error
CRITICAL = log.critical


def log_it(level: Callable, msg: str) -> None:
    level(msg)


if __name__ == "__main__":
    log_it(DEBUG, "This is a debug message.")
    log_it(INFO, "This is an info message.")
    log_it(WARNING, "This is a warning message.")
    log_it(ERROR, "This is an error message.")
    log_it(CRITICAL, "This is a critical message.")
    