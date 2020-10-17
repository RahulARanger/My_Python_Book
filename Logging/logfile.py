import logging
'''
logging.basicConfig() has 

level: The root logger will be set to the specified severity level.
filename: This specifies the file.
filemode: If filename is given, the file is opened in this mode. The default is a, which means append.
format: This is the format of the log message.

'''
logging.basicConfig(level=logging.DEBUG,filename='check.log',filemode='a')
logging.info('this is a info box')