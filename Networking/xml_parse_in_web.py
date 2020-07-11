# this is the program that reads the xml that has been embedeed in website
# and finds the numbers in the <comment> and then finds the sum of them
# Some of the sample websites are the  http://py4e-data.dr-chuck.net/comments_42.xml
# and http://py4e-data.dr-chuck.net/comments_488273.xml
import urllib.request
import xml.etree.ElementTree as et
import functools
website=input('Enter the Website link: ')
sum=0
hand=urllib.request.urlopen(website)
data=''''''
for i in hand:
    data+=i.decode()
tree=et.fromstring(data)
lst=tree.findall('comments/comment')
numbers=[]
for i in lst:
    numbers.append(i.find('count').text)
numbers=list(map(lambda x:int(x),numbers))
if len(numbers)!=0:sum=functools.reduce(lambda x,y:x+y,numbers)
else:pass
print(sum)