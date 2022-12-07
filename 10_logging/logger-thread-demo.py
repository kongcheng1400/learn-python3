import logging
from logging import DEBUG, INFO, WARNING, ERROR, CRITICAL
import time
import threading
import sys




logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def logTest():
    while True:
        time.sleep(2)
        logger.info(f'in current Thread: {threading.current_thread().name}')

myThread = threading.Thread(name='test_theread', target=logTest, daemon=True)
myThread.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    logger.warning('Ctrl-C pressed. Shutting down...')
    sys.exit(0)
    
