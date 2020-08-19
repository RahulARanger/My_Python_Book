def factorial(n):
    if n==0 or n==1: return 1
    else:return n*factorial(n-1)
def product(lst,n): 
    p=1
    for i in range(n): 
        p*=lst[i]
    return p
def sum_(lst,n):
    s=0
    for i in range(n):
        s+=lst[i]
    return s
n=int(input('Enter the Value of n: '))
lst=[int(i) for i in input('Enter the list element: ').split()]
p=int(product(lst,n+2)/factorial(n))
s=int(sum_(lst,n+2)-((n*(n+1))/2))
sq=s*s-2*p
diff=int((sq-2*p)**0.5)
x=(s+diff)/2
y=s-x
print(int(x),int(y))