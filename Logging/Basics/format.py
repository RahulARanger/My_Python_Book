import logging

# Refer this for more attributes: https://docs.python.org/3/library/logging.html#logrecord-attributess
logging.basicConfig(level=logging.DEBUG, filename="basics.log", format="%(levelname)s: %(asctime)s => %(message)s")

# we can also control the formats for the log file

logging.debug('This is a debug message')  # won't be printed
logging.info('This is an info message')  # won't be printed
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
