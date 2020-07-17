def top_cone(n):
    str='H'
    odd=[]
    a=1+(n-1)*2
    for i in range(1,n+1):
        odd.append(int(1+(i-1)*2))  
    for i in odd:
        print((i*str).center(a))
    return a    
def bottom_cone(n,y):
    h='H'
    a=(1+(n-1)*2)
    spaces=' '*y
    spaced=' '
    start=0
    for i in range(n):
        print(spaces,end='')
        total=start*spaced
        total+=h*a
        print(total)
        a-=2
        start+=1
def mpillar(n,a):
    odd_number=int(((n-1)/2)+1)
    lengthofpillar=int(((odd_number*n)-odd_number)/2)
    lefts_space=(a-n)//2
    ls=' '*lefts_space
    h='H'
    h=n*h
    spaces=3*n
    spaces=' '*spaces
    total=h
    total+=spaces+h  
    totalwol=total
    total=ls+total
    totale=totalwol.replace(' ','H')    
    totale=ls+totale
    for i in range(lengthofpillar):
        print(total)
    for i in range(odd_number):
        print(totale)
    for i in range(lengthofpillar):
        print(total)
    return len(total)-len(h)-len(ls)    

def design(n):
    x=top_cone(n)
    y=mpillar(n,x)
    bottom_cone(n,y)

if __name__ == "__main__":
    n=int(input())
    design(n)
