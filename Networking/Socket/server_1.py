import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(), 6969))  # binding the socket with the name and port

server.listen(2)  # 2 connections at max in queue
# https://pythontic.com/modules/socket/listen#:~:text=Calling%20listen()%20makes%20a,method%20on%20the%20server%20socket.&text=This%20denotes%20maximum%20number%20of,socket%20by%20the%20operating%20system.
conn, add = server.accept()  # accepts one socket and then quits

print(conn)  # of the client socket
print(add)  # add of the client computer, here same as server if used locally
