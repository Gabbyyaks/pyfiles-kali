import logging
import logging.config

logging.config.fileConfig('logging.config')

logger = logging.getLogger('simpleExample')
logger.debug('this is a debug message')

