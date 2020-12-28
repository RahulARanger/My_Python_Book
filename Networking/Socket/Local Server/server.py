import socket
import sys,threading
class Server:
    def __init__(self):
        self.host='127.0.0.1' # ? static ip address for the local server
        self.port=4567 # ? some random 4-digit number. but they shouldn't match with the predefined port numbers
        self.search=True
        try:self.obj=socket.socket(socket.AF_INET,socket.SOCK_STREAM) # AF_INET tells socket about the IPV_4 protocol and socket.SOCK_STREAM for chooosing TCP protocol
        except  socket.error as e:
            print(e)
            sys.exit(0)
        self.bind_connection()
    def bind_connection(self):
        # TODO: binding connection helps us to bind the socket with host and port so that data can have from address
        try:self.obj.bind(self.host,self.port)
        except socket.error as e:
            print(e) # ? mostly happens when the self.host is invalid or self.port is replaceing the predefined port numbers
            sys.exit(0)
    