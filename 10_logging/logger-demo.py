import logging
import argparse
from logging import DEBUG, INFO, WARNING, ERROR, CRITICAL

parser = argparse.ArgumentParser(description='logging testing.')
parser.add_argument('--loglevel', default='INFO', help='log level',
        choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG'])
parser.add_argument('--logfile', default='log.txt', help='specify the log file')
args = parser.parse_args()

logging.basicConfig(filename=args.logfile, filemode='w', encoding='utf-8',
        format='%(asctime)s %(message)s', level=args.loglevel)
logger = logging.getLogger(__name__)
logger.setLevel(args.loglevel)
log_console_handler = logging.StreamHandler()
log_console_handler.setLevel(args.loglevel)
log_console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log_console_handler.setFormatter(log_console_formatter)
logger.addHandler(log_console_handler)

logger.info(f'loglevel={args.loglevel}, logfile={args.logfile}')
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
