import logging
logger = logging.getLogger('data_log')
logger.setLevel(69)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(66)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')