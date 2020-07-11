# not works for all tho
import urllib.request
website=input('Enter the Link: ')
try:
    hand=urllib.request.urlretrieve(website,'test2.mp4')
except:
    print('No Connection or for some other reasons')    
