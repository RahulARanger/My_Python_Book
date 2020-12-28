import socket
import threading,sys
class Client:
    def __init__(self):
        self.host="localhost" # * another name for the 127.0.0.1
        self.port=4567 # ! this must match with all the clients and the server
        try:self.obj=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        except socket.error as e:
            print(e)
            sys.exit(0)
        self.bind_connection()
    def bind_connection(self):
        try:self.bind(self.host,self.port)
        except socket.error as e:
            print(e)
            sys.exit(0)