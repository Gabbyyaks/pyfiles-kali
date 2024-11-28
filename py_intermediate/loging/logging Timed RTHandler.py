import logging
import time
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# when- s=second, m=min, h=hour, D,=days.. - w0= mon, w1=tue, w2=wed

handler = TimedRotatingFileHandler("Time_test.log", when='S', interval=5, backupCount=4)
logger.addHandler(handler)

for _ in range(5000):
    logger.info('Timed message')
    time.sleep(5)



