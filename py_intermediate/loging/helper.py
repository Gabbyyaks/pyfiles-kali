import logging

# Basic loging config - types (file config - dict  config)

logger = logging.getLogger(__name__)
logger.info("this is a logging message")

# Log handler - (objects) responsible for dispatching the appropriate log message to handler specific destination

# create handler
stream_h = logging.StreamHandler()      # logs stream
file_h = logging.FileHandler('file.log')    # log file

# level and format of handler
stream_h.setLevel(logging.WARNING)      # logs level warning and above
file_h.setLevel(logging.ERROR)          # logs into a file

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')     # setting formatter
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

# adding handler to logger
logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning("this is a warning")
logger.error("this is an error")


# Capturing stack traces in log




