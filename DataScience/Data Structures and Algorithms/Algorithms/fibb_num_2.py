# this alg. is good (speedy) when it comes to find the nth term
import time
import itertools
def nth_series(n):
    prev=0
    curr=1
    time=2
    if n<=time and n>0:
        return prev if n==1 else curr
    for i in itertools.count(0):
        time+=1
        store=curr
        curr+=prev
        prev=store
        if time==n:return curr
n=int(input('Enter the term to be searched in the fibb. series: '))
check=time.time()        
checked=nth_series(n)
print('{}th time  in the fibb. series is : {} '.format(n,checked))
print(time.time()-check)