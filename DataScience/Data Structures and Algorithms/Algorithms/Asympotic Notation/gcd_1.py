import time
def gcd(a,b):
    check=min([a,b])
    gcd_ans=1
    for i in range(2,check+1):
        if a%i==0 and b%i==0:
            gcd_ans=i
    return gcd_ans        
a,b=[int(i) for i in input().split()]
check=time.time()
print(gcd(a,b))
print(time.time()-check)