# this is the answer for the question 5 of the week 2 assignment
import itertools
def last_fibb_series(n,m):
    c,p=1,1
    for i in range(3,n+1):
        p,c=c,c+p
    return c%m
def create_series(n,m):
    check=[0,1,1,2] 
    c,p=1,1
    ans=[0,1,1]
    count=0
    for i in itertools.count(0):
        p,c=c,p+c
        ans.append(c%m)
        count+=1
        if len(ans)>=4:
            if ans[count-4:count]==check and count>4:break            
    return ans
n,m=[int(i) for i in input().split()]
check=[]
if m!=2:
    check=create_series(n,m)
    check=check[:-7]
else:
    check=[0,1,1]
print(check[n%len(check)])