import threading
import socketserver
import time
import queue
import logging
import argparse
import socketscpi
from logging import DEBUG, INFO, WARNING, ERROR, CRITICAL

logger = logging.getLogger(__name__)
close_connections = False



class Disconnected(Exception): pass

# handle the instruments.
class InstrumentHandler(threading.Thread):
    def __init__(self, ip_address, name, isDaemon, msgQ_from_island, msgQ_to_island) -> None:
        super().__init__(name=name+' handler', daemon=isDaemon)
        self.ip = ip_address
        self.port = 5025
        self.name = name
        self.queue_from_island = msgQ_from_island
        self.queue_to_island = msgQ_to_island
        try:
            self.instrument = socketscpi.SocketInstrument(self.ip)
        except Exception as err:
            logger.critical(f'connection to instrument {self.name} at ipaddr={self.ip} failed:{err}')
            raise ConnectionError(f'instrument {self.name}')
        logger.info(f'connection to {self.name} established with {self.ip}')
        res_err = self.instrument.query('syst:err?')
        res_idn = self.instrument.query('*idn?')
        logger.info(f'instrument identified as: {res_idn}, and status: {res_err}')

    def run(self) -> None:
        while True:
            if self.instrument.socket.fileno() == -1:
                break
            res = None
            if not self.queue_from_island.empty():
                cmd = self.queue_from_island.get()
                logger.log(INFO, 'from island cmd:{}'.format(cmd))
                if '?' in cmd:
                    #res = r'+0,"No error"'
                    res = self.instrument.query(cmd)
                    logger.log(INFO, 'responded with:{}'.format(res))
                else:
                    self.instrument.write(cmd)
                    logger.log(INFO, 'write to instrument:{}'.format(cmd))
            if res:
                self.queue_to_island.put(res)


class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    def setup(self) -> None:
        logger.info(f'this connection started:{self.client_address}')
        self.queue_from_island = queue.Queue()
        self.queue_to_island = queue.Queue()
        #create the connection the instrument
        self.instrument_handler_thread = InstrumentHandler(self.server.instrument_ip_address, 'N9020', True, self.queue_from_island, self.queue_to_island)
        return super().setup()

    def handle(self):

        try:
            self.instrument_handler_thread.start()
            send_thread = threading.Thread(name='sub-send-thread', target=self.send, daemon=True)
            send_thread.start()
            receive_thread = threading.Thread(name='sub-receive-thread', target=self.receive, daemon=True)
            receive_thread.start()
        except Exception as err:
            logger.warning(f'in handle {err}')
            return 
        while True:
            if not self.instrument_handler_thread.is_alive():
                logger.critical(f'cant create the connection to insturment {self.instrument_handler_thread.name}')
                break
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
                #response = bytes("{}".format(data), 'ascii')
                if type(data) == str:
                    newline = '\n'
                    reply = data + newline
                    reply = reply.encode('utf-8')
                    
                logger.info(f'to Island responded with data:{reply}')
                self.request.sendall(reply)
    # the clean process
    def finish(self) -> None:
        logger.info(f'this connection finished:{self.client_address}, and close the instrument')
        self.instrument_handler_thread.instrument.close()
        return super().finish()


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    def __init__(self, addr, instrument_ip_address, RequestHandler) -> None:
        socketserver.ThreadingMixIn.__init__(self)
        socketserver.TCPServer.__init__(self, addr, RequestHandler)
        self.instrument_ip_address = instrument_ip_address


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='logging testing.')
    parser.add_argument('--loglevel', default='INFO', help='log level',
                    choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG'])
    parser.add_argument('--logfile', default='log.txt',
                    help='specify the log file')
    args = parser.parse_args()

    logging.basicConfig(filename=args.logfile, filemode='w', encoding='utf-8',
                    format='%(asctime)s %(message)s', level=args.loglevel)
    logger.setLevel(args.loglevel)
    log_console_handler = logging.StreamHandler()
    log_console_handler.setLevel(args.loglevel)
    log_console_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    log_console_handler.setFormatter(log_console_formatter)
    logger.addHandler(log_console_handler)

    print(f'loglevel={args.loglevel}, logfile={args.logfile}')
    # Port 0 means to select an arbitrary unused port
    # Port 5205 is the usually instrument SCPI-socket service port.
    HOST, PORT = "localhost", 5025
    instrument_address, instrument_port = '10.86.134.71', 5025
    instrument=socketscpi.SocketInstrument(instrument_address)
    res = instrument.query('*opc?')
    logger.info(res)
    res = instrument.query('syst:err?')
    logger.info(res)
    idn = instrument.query('*idn?')
    logger.info(res)
    res = instrument.close()
    logger.info(f'instrument{idn} checked successful on {instrument_address} {instrument_port}')


    server = ThreadedTCPServer((HOST, PORT), instrument_address, ThreadedTCPRequestHandler)
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
