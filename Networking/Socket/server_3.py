from multiprocessing.connection import Listener
import socket


server = Listener((socket.gethostname(), 6969))
connection = server.accept()
print(connection, server)

for _ in range(3):
    print(connection.recv())

connection.close()
server.close()
