import logging
logging.basicConfig(level=logging.DEBUG)
#? level sets the minimum security level
# * basic security level (debug<info<warning<error<critical)
# ! by default warning is the default for the level
logging.info('This is info log')
logging.debug('This is a debug message') 
logging.info('This is an info message') 
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')