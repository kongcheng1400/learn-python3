#Echo server program
import socket
import sys

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print(f'listening on port={PORT}')
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        print('conn=', conn)
        while True:
            try:
                data = conn.recv(1024)
                if not data: break
                conn.sendall(data)
            except ConnectionError as err:
                print(f'@@Exception of err:{err}')
                print(f'@@after exception conn = {conn}')
                conn.close()
                print(f'@@conn closed conn = {conn}')
                break
            except KeyboardInterrupt:
                print('ctrl+C detected.')
                break
            except:
                raise