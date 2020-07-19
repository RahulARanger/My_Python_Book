# using the euclidean formuale best alg. (time efficient)
import time
def gcd(a,b):
    if b>a:a,b=b,a
    check=a%b
    if check==0:return b
    else: 
        return gcd(b,check)
a,b=[int(i) for i in input().split()]
checked=time.time()
print(gcd(a,b))
print(time.time()-checked)