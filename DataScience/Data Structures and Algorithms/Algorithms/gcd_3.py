def gcd(a,b):
    if b>a:a,b=b,a
    if a%b==0:return b
    else:
        return gcd(b,a%b)
a,b=[int(i) for i in input().split()]
print(gcd(a,b))