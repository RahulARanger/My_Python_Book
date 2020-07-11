# this program goes through the body of the web page and finds the numbers and also their sum
# there are two useful links http://py4e-data.dr-chuck.net/comments_42.html and other one is http://py4e-data.dr-chuck.net/comments_488271.html try this
sum=0
import re
import functools as r
import urllib.request
website=input('Enter the website link: ')
hand=None
try:
    hand=urllib.request.urlopen(website)
    for i in hand:
        line=i.decode().strip()
        numbers=re.findall('>([0-9]+)',line)
        numbers=list(map(lambda x:int(x),numbers))
        if len(numbers)!=0:sum+=r.reduce(lambda x,y:x+y,numbers)
        else:pass
except:
    print('No connections or due to some errors like link error,etc...')
    quit()
finally:
    hand.close()    
print(sum)    