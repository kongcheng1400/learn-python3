import threading
import time
import logging
import sys

logging.basicConfig(level=logging.DEBUG)
class MyException(Exception): pass


class myThread(threading.Thread):
    def __init__(self, threadID, name, counter) -> None:
        super().__init__()
        self.threadID = threadID
        self.name = name
        self.counter = counter
    
    def run(self):
        i = 0
        while True:
            try:
                time.sleep(3)
                i = i + 1
                current_thread_name = threading.current_thread()
                print(f'running in {current_thread_name} at counter {i}')
                if i == self.counter:
                    raise MyException('counter expired')
            except MyException as err:
                print(f'Trigger an exception:{err}')
                raise MyException


thread = myThread(1, 'mythread', 5)
#thread.run()
thread.daemon=True
thread.start()
try:
    while True:
        time.sleep(5)
        logging.warning(threading.enumerate())
except KeyboardInterrupt:
    logging.warning('Ctrl-C pressed. Shutting down...')
    sys.exit(0)