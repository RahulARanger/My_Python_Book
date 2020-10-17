
# TODO: script taken from the:  https://stackoverflow.com/questions/11232230/logging-to-two-files-with-different-settings
import logging
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')


def setup_logger(name, log_file, level=logging.INFO):
    handler = logging.FileHandler(log_file)        
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger
logger = setup_logger('first_logger', 'first_logfile.log')
logger.info('This is just info message')
super_logger = setup_logger('second_logger', 'second_logfile.log')
super_logger.error('This is an error message')