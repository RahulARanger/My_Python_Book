import re
results=['Jan 31 00:09:39 ubuntu.local ticky: ERROR Permission denied while closing ticket (ac)','Jan 31 00:09:39 ubuntu.local ticky: INFO Created ticket [#4217] (mdouglas)']
users=[]
for i in results:
    if 'ERROR' in i:
        print(re.search(r'ERROR ([^(]+)',i)[1])
    users.append(re.search(r'\(([^ ]+)\)',i)[1])
print(users)    