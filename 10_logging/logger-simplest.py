import logging
from logging import DEBUG, INFO, WARNING, ERROR, CRITICAL

logger = logging.getLogger(__name__)
#logger.setLevel(logging.DEBUG)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger.info('basic test')
logger.warning('basic test')