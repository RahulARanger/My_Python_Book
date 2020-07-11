import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re
# Ignore SSL certificate errors

def open_web(website,c):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    url=website
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    count=0
    for tag in tags:
        count+=1
        if count==c:
          return tag.get('href', None)

website=input('Enter the website Link: ')
count,position=int(input('Enter the Count: ')),int(input('Enter the Position Index: '))
for i in range(count):
    website=open_web(website,position)
answer=re.findall('known_by_(.*).html',website)    
print(answer[0])
