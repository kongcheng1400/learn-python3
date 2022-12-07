import socket
import time
import threading
import sys

ip, port = "localhost", 30031
message = 'hello, socket!'

def echo_client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    for i in range(20):
        time.sleep(2)
        try:
            sock.sendall(bytes('{} cnt {}'.format(message, i), 'ascii'))
            response = str(sock.recv(1024), 'ascii')
            print("Received: {}".format(response))
        except ConnectionError as err:
            sock.shutdown(socket.SHUT_RDWR)
            print(f'catched exception of err={err}')
            print(f'connection err and sock={sock}, fielno={sock.fileno()}')
            sock.close()
            print(f'socket closed and sock={sock}, fielno={sock.fileno()}')
            break

    
myThread = threading.Thread(target=echo_client, name='mythread', daemon=True)
myThread.start()
try:
    print('Ctrl+C to exit......')
    while True:
        time.sleep(2)
        print(threading.enumerate())
except KeyboardInterrupt:
    print('Ctrl+C interruption and exit...')
    sys.exit(0)
