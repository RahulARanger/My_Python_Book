import logging
logging.basicConfig(level=logging.DEBUG,filename='test2.log',filemode='a',format='%(asctime)s  %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.info('Gonna Start')
