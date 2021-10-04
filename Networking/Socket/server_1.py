import socket

port = 6969

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(
    (socket.gethostname(), port)
)  # binding the socket to host here local machine
server.listen(1)  # allows only one client at a time


conn, addr = server.accept()
print(conn)
print(addr)  # socket object and address of the client
# after this that conn socket is dead
