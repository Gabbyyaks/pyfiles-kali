# capturing stack traces
import logging
from logging import DEBUG
from logging.handlers import RotatingFileHandler
from logging.handlers import TimedRotatingFileHandler

from sys import exc_info
import traceback

from asysocks.intercepting.monitors.rawlogging import handler

try:
    a = [1, 2, 3]
    val = a[3]
except IndexError as e:
    logging.error(e, exc_info=True)  # logging.error(e) - default ** exc_info=True - full stack trace error
finally:
    logging.error('this is the error %s', traceback.format_exc())   # method 2 - unknown error using traceback to get full info

# Rotating file handler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Roll over after 2kb, and keep backup logs - app.log1, app.log2 .. etc

handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
logger.addHandler(handler)

for _ in range(6000):
    logger.info("This is a log message ")


# TimedRotating File handler




















