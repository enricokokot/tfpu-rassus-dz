import logging

logger = logging.getLogger("logger")
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler('logs/app_log.log')
file_handler.setLevel(logging.WARNING)

formatter_file = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
formatter_console = logging.Formatter('%(message)s')
console_handler.setFormatter(formatter_console)
file_handler.setFormatter(formatter_file)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.debug('This is a debug message.')
logger.info('This is an info message.')
logger.warning('This is a warning message.')
logger.error('This is an error message.')
logger.critical('This is a critical message.')