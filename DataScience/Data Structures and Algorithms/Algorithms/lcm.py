
def gcd(a,b):
    if b>a:a,b=b,a
    if a%b==0:return b
    else:
        return gcd(b,a%b)
def lcm(a,b):
    if a==0 or b==0: return 0
    elif a==1 or b==1: return a*b
    ans=1
    while(True):
        check=gcd(a,b)
        if check==1:
            ans*=(a*b)
            break
        else:
            a//=check
            b//=check
            ans*=check
    return ans

a,b=[int(i) for i in input().split()]
print(lcm(a,b))  
     
