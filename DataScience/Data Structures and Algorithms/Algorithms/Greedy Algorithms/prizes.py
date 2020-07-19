# this is the answer for the assignment 8 for the week3 
import itertools
import sys
def find_it(n):
    count=1
    lst=[]
    for _ in itertools.count(0):
        check=count*(count+1)
        check/=2
        lst.append(count)
        if check==n:return lst[:-1]
        elif check>n:return lst[:-1]
        count+=1
n=int(input())
if n==1:
    print('1\n1')
    sys.exit(0)
lst=find_it(n)
if sum(lst)==n:pass
else:
    if n-sum(lst)>max(lst):
        lst.append(n-sum(lst))
    else:
        lst.remove(max(lst))
        lst.append(n-sum(lst))    
print(len(lst))
[print(i,end=' ') for i in lst]
