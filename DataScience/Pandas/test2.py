import re
n=int(input())
A={int(i) for i in input().split()}
N=int(input())
for i in range(N):
    text=input()
    sub={int(i) for i in input().split()}
    if len(re.findall(r'^update',text))!=0:
        A.update(sub)
        #print('*')
    elif 'intersection_update' in text:
        A.intersection_update(sub)
        #print('%')
    elif len(re.findall(r'^difference_update',text))>0:
        A.difference_update(sub)
        #print('#')
    else:
        A.symmetric_difference_update(sub)
        #print('$')
    #print(A)    
print(sum(A))                



