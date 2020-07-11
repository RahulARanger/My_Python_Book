import socket
try:
    soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host='localhost'
    port=6969
    soc.connect((host,port))
    while True:
        s=soc.recv(1024)
        m=s.decode()
        if len(m)==0:break
        print(m)

    soc.close()
except:
    print('Error')        