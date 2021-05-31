# Sample: http://py4e-data.dr-chuck.net/comments_488274.json

import urllib.request
import json

website = input()
data = ''''''
sum_ = 0
h = urllib.request.urlopen(website)
for i in h:
    data += i.decode().strip() + '''\n'''
loaded = json.loads(data)
for i in range(len(loaded["comments"])):
    sum_ += (loaded['comments'][i]['count'])
print(sum_)
