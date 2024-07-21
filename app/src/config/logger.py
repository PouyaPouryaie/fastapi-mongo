import logging
import sys

# get logger
logger = logging.getLogger()


# create formatter
formatter = logging.Formatter(fmt="%(asctime)s - %(levelname)s - %(message)s", datefmt='%d-%b-%y %H:%M:%S')

# create handler
stream_handler = logging.StreamHandler(sys.stdout)

# set formatter
stream_handler.setFormatter(formatter)

# add handler to the logger
logger.handlers = [stream_handler]
# logger.addHandler(stream_handler)

# set log level
logger.setLevel(logging.INFO)