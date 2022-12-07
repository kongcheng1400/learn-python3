import threading
import socketserver
import time
import queue
import logging
from logging import DEBUG, INFO, WARNING, ERROR, CRITICAL
import logging
level    = logging.INFO
format   = '%(asctime)s-%(name)s-%(levelname)s-%(message)s'
log_file = __name__ + '.log'
handlers = [logging.FileHandler(log_file), logging.StreamHandler()]
logging.basicConfig(level = level, format = format, handlers = handlers)
logger = logging.getLogger(__name__)
close_connections = False

cmd_map = {
    '*idn?': 'manufacture,type,SN,version',
    'opc?': '+1',
    '*ESR?': '+0'
}

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    def setup(self) -> None:
        logger.info(f'this connection started:{self.client_address}')
        self.queue_from_island = queue.Queue()
        self.queue_to_island = queue.Queue()
        #create the connection to the instrument here.
        
        return super().setup()

    def handle(self):

        try:
            send_thread = threading.Thread(name='sub-send-thread', target=self.send, daemon=True)
            send_thread.start()
            receive_thread = threading.Thread(name='sub-receive-thread', target=self.receive, daemon=True)
            receive_thread.start()
        except Exception as err:
            logger.warning(f'in handle {err}')
            return 
        while True:
            if close_connections or self.request.fileno() == -1:
                logger.warning(f'server is closing all connections')
                break
            
    def receive(self):
        while True:
            data = None
            try:
                data = str(self.request.recv(1024), 'ascii')
                logger.info(f'from island{self.client_address}:{data}')
            except ConnectionError as err:
                self.request.close()
                logger.warning(f'client {self.client_address} aborted connection with error {err}')
                break
            except OSError as err:
                self.request.close()
                logger.warning(f'connection {self.client_address} invalid with error {err} and exit')
                break
            except:
                raise
            if data:
                self.queue_from_island.put(data)
            else:
                self.request.close()
                break
    
    def send(self):
        cur_thread = threading.current_thread()
        while True:
            if self.request.fileno() == -1:
                logger.warning(f'connection from {self.client_address} closed and exit{cur_thread}')
                break
            if not self.queue_to_island.empty():
                data = self.queue_to_island.get()
                response = bytes("{}: {}".format(
                    cur_thread.name, data), 'ascii')
                logger.info(f'to Island responded with data:{response}')
                self.request.sendall(response)
    
    def cmd_analyze(self):
        while True:
            #
            if self.request.fileno() == -1:
                break
            if not self.queue_to_island.empty():
                cmd = self.queue_from_island.get()







    def finish(self) -> None:
        logger.info(f'this connection finished:{self.client_address}')
        return super().finish()


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    def __init__(self, addr, RequestHandler) -> None:
        socketserver.ThreadingMixIn.__init__(self)
        socketserver.TCPServer.__init__(self, addr, RequestHandler)
        self.msgQue = queue.Queue()


if __name__ == "__main__":
    # Port 0 means to select an arbitrary unused port
    HOST, PORT = "localhost", 5025

    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    with server:
        ip, port = server.server_address
        print(
            f'server cfg: addressFamily={server.address_family} ip={ip} port={port}')
        print(
            f'server cfg: timeout={server.timeout}, sockettype={server.socket_type}')
        # Start a thread with the server -- that thread will then start one
        # more thread for each request
        server_thread = threading.Thread(target=server.serve_forever)
        # Exit the server thread when the main thread terminates
        server_thread.daemon = True
        server_thread.start()
        logger.info(f'Server loop running in thread:{server_thread.name}')
        try:
            while True:
                time.sleep(5)
                logger.info(threading.enumerate())
        except KeyboardInterrupt:
            logger.warning('Ctrl-C pressed. Shutting down...')
            close_connections = True
            server.shutdown()
