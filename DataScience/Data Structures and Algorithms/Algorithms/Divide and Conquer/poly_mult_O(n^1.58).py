from  Polynomial_Mult import get_eq,print_eq,mult
import collections
# Refer this website for more exp. : https://www.geeksforgeeks.org/multiply-two-polynomials-2/
# imported some methods(get_eq() and print_eq() and mult()) from Polynomial_Mult.py file 
def add__(eq1,eq2):
    ans=collections.Counter()
    ans.update(eq1)
    ans.update(eq2)
    return dict(ans)
def sub__(eq1,eq2):
    ans=collections.Counter()
    ans.update(eq1)
    a_=collections.Counter()
    a_.update(eq2)
    return dict(ans-a_)
def splitup(eq,lst):
    mid=len(lst)//2
    lst_l=lst[:mid]
    lst_r=lst[mid:]
    new_eq_1={}
    new_eq_2={}
    for i in range(len(lst_l)):
        new_eq_1[i]=eq[lst_l[i]]
    for j in range(len(lst_r)):
        new_eq_2[j]=eq[lst_r[j]]
    return new_eq_1,new_eq_2
import time
a,b=get_eq('A'),get_eq('B')
n=max([max(a.keys()),max(b.keys())])+1
print('The Given Equations are: ')
print_eq(a),print_eq(b)
check=time.time()
lst=list(a.keys())
lst.sort()
d0,d1=splitup(a,lst)
lst=list(b.keys())
lst.sort()
e0,e1=splitup(b,lst)
'''
    According to Karatsuba approach,
            A(x)*B(x)=d(0)*e(0) + ([(d(0)+d(1))*(e(0)*e(1))]-[d(1)*e(1)]-[d(0)*e(0)])X^n/2 + d(1)*e(1)*X^n
'''
_1=mult(d0,e0)
_2=mult(d1,e1)
__2=mult(_2,{n:1})
_3=mult(add__(d0,d1),add__(e1,e0))
__1=add__(_1,__2)
_2=add__(_1,_2)
_4=sub__(_3,_2)
__2=mult(_4,{n//2:1})
ans=add__(__1,__2)
print('The Product of the two given equations are: ')
print_eq(ans)
print('Time Consumed is:',time.time()-check)

# Time Complexity of this algorithm is O(n^1.58) refer the above given website to know how