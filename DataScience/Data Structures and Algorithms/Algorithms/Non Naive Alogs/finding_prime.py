
# TODO: Normally it's enough to check the first root(n)+1 for the factors
def check_prime(n):
    if n<=3:return True
    last=int((n**0.5))+1
    for i in range(2,last+1):
        if n%i==0:
            return False # it isn't virigin
    return True # yEs it is Virgin

'''
Sample Problem:

A positive integer m is a prime product if it can be written as p×q, where p and q are both primes. .

Write a Python function primeproduct(m) that takes an integer m as input and returns True if m is a prime product and False otherwise. (If m is not positive, your function should return False.)
'''

def primeproduct(m):
    last=int((m**0.5))+1
    facs=[]
    for i in range(2,last+1):
        if m%i==0:
            facs.append(i)    
            facs.append(m//i) 
    facs=list(set(facs))
    if len(facs)!=2:return False
    for i in facs:
        if not check_prime(i):            
            return False
    return True

if __name__=='__main__':
    m=int(input('Enter the Number: '))
    print(primeproduct(m))