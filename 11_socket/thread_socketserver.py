import threading
import socketserver
import os
import time
import logging
from logging import DEBUG, INFO, WARNING, ERROR, CRITICAL
level       = logging.DEBUG
format      = '%(asctime)s[%(levelname) 8s] %(message)s'
file_name   = os.path.basename(__file__).split('.')[0]
log_file    = file_name + '.log'
handlers = [logging.FileHandler(log_file, mode='w'), logging.StreamHandler()]
logging.basicConfig(level = level, format = format, handlers = handlers)
logger = logging.getLogger(file_name)
close_connections = False


cmd_reply_map = {
    "*IDN?": "Keysight Technologies,U2049XA,DVT_proxy,A0.0.0",
    "SERV:SENS1:TYPE?": "U2049XA",
    "stat:dev:cond?": "+2",
    "*ESR?": "0",
    "*OPC?": "1",
}

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    def setup(self) -> None:
        logger.info(f'client connection:{self.client_address},host sockname: {self.request.getsockname()},host blocking: {self.request.getblocking()}')
        return super().setup()

    def handle(self):
        instr_name = self.server.server_name
        if (self.server.sema.acquire(blocking=True, timeout=5) == False):
            logger.critical(f'> 2 connections from client :{self.client_address}, denying')
        else:
            logger.info(f'incoming connection from island started:{self.client_address}')
            while True:
                data = None
                res = None
                if self.request.fileno() == -1:
                    logger.critical(f'socket connections from Island closed, exit')
                    break
                if close_connections:
                    logger.critical(f'server is closing all connections')
                    break
                try:
                    data = str(self.request.recv(1024), 'ascii')
                    if data == '' or data is None:
                        logger.critical(f'read empty data from socket island {self.client_address}, exit')
                        break  
                        
                    datalist = data.strip().split('\n')
                    nbr = len(datalist)
                    logger.info('')
                    logger.info('---> Raw msg with {} cmds from island {}:{!a}'.format(nbr, self.client_address, data))

                    for idx, cmd in enumerate(datalist):
                        logger.debug(f'procssing cmd[{idx}] to {instr_name}:{cmd}')
                        if not cmd == '':
                            res = self.cmd_processing(cmd)
                            if type(res)==str:
                                reply = (res+'\n').encode('utf-8')
                                logger.info(f'<--- Response for cmd[{idx}] to island:{reply}')
                                self.request.sendall(reply)
                except ConnectionError as err:
                    self.request.close()
                    logger.warning(f'connection error with error {err}')
                    break
                except OSError as err:
                    self.request.close()
                    logger.warning(f'socket invalid with error: {err} and exit')
                    break
                except Exception as err:
                    self.request.close()
                    logger.warning(f'exception catched with error: {err} and exit')
                    break

    def cmd_processing(self, cmd):
        res = cmd_reply_map.get(cmd, None)
        return res

    def finish(self) -> None:
        logger.info(f'this connection finished:{self.client_address}')
        #release the semaphore
        self.server.sema.release()
        return super().finish()

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    def __init__(self, addr, server_name, RequestHandler) -> None:
        socketserver.ThreadingMixIn.__init__(self)
        socketserver.TCPServer.__init__(self, addr, RequestHandler)
        self.server_name = server_name
        # only two connecitons to proxy is allowed.
        self.sema = threading.Semaphore(2)


if __name__ == "__main__":
    # Port 0 means to select an arbitrary unused port
    HOST, PORT = "localhost", 5025

    server = ThreadedTCPServer((HOST, PORT), "DVT Proxy server",ThreadedTCPRequestHandler)
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
            logger.warning('Ctrl-C pressed. Shutting down server...')
            close_connections = True
            server.shutdown()
