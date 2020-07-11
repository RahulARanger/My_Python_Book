import urllib.request
try:
    check=urllib.request.urlopen('https://www.google.com')
    print('U are connected to the Internet')
except:
    print('U are not connected to the Internet')    