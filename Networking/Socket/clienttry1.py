import socket
class client:
    def __init__(self):
        HOST='127.0.1.1'
        port=65432
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
            s.bind(('127.0.1.2',65431))
            s.connect((HOST,port))
            s.sendall(b'Hello World')
            data=s.recv(1024)
        print('Received',repr(data))
client()