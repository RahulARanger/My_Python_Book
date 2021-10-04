import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((socket.gethostname(), 6969))
server.listen()

conn, addr = server.accept()

for index in range(10):
    print(conn.recv(2))

server.close()  # a way to close the connection
