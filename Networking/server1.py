import socket
try:
    host='localhost'
    port=6969
    #print(socket.gethostbyname(host))
    soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    soc.bind((host,port))
    soc.listen(1)
    c,addr=soc.accept()
    msg='Hello there'.encode()
    c.send(msg)
    msg='How are You'.encode()
    c.send(msg)
    c.close()
    soc.close()

except:
    print('Error')