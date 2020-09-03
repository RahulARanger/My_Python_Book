import urllib.request
link=input('Enter the link for the image in the internet: ')
try:
    download=urllib.request.urlretrieve(link,'test1.html')
except:
    print('The link is not working!!!')