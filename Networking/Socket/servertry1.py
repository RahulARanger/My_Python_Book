import socket 
class server():
    def __init__(self):
        HOST='127.0.1.1'
        port=65432
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
            s.bind((HOST,port))
            s.listen()
            conn,addr=s.accept()
            while conn:
                print('connected by ',addr)
                while True:
                    data=conn.recv(1024)
                    if not data:
                        break
                    conn.sendall(data)
                break

server()