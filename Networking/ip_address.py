import socket
website=input('Enter the website link: ')
try:
    addr=socket.gethostbyname(website)
    print('The Ip address of the given website is: ',addr)
except:
    print('The given website doesn\' exist')