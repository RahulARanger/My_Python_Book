import logging

# This module is used to create the logs of the file

# Refer this for more basics: https://docs.python.org/3/howto/logging.html#logging-basic-tutorial

'''
DEBUG
INFO
WARNING
ERROR
CRITICAL

This are the 5 basic logging messages that can be created (using the logging)

'''
logging.debug('This is a debug message')  # won't be printed
logging.info('This is an info message')  # won't be printed
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

# ? Levels in the logging has a order

# debug < info < warning < error < critical (level= ) sets the threshold

# This threshold will let the levels below it to be ignored and greater or equal to it to be logged

# by default threshold is set to warning
