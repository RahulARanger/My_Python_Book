def last_fibb_series(n):
    c,p=1,1
    for i in range(3,n+1):
        p,c=c,c+p
    return c%10
check=[]
for i in range(1,61):
    if i<2: 
        check.append(1 if i==1 else 0)
    else:
        check.append(last_fibb_series(i))    
n=int(input())
if n<=0:print(0)
else:
    n-=1
    print(check[n%60])
