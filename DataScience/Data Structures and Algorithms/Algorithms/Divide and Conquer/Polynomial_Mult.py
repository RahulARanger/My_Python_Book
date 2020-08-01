import time
def mult(a,b):
    new_eq={}
    for i in a:
        for j in b:
            index=i+j
            new_eq[index]=new_eq.get(index,0)+a[i]*b[j]
    return new_eq        
def get_eq(ch):
    terms=int(input('Degree of the Equation {} :'.format(ch)))
    eq={}
    for i in range(terms,-1,-1):
        deg=int(input('Enter the Coeff. of {} degree: '.format(i)))
        eq[i]=deg
    return eq    
def print_eq(eq):
    lst=list(eq.keys())
    lst.sort(reverse=True)
    for i in range(len(lst)):
        if eq[lst[i]]==0:continue
        if i!=0:print(' + ' if eq[lst[i]]>0 else ' - ',end='')
        if lst[i]==0:print('{}'.format(eq[lst[i]]))
        else:print('{}X^{}'.format(eq[lst[i]],lst[i]),end='')
if __name__=='__main__':
    a,b=get_eq('A'),get_eq('B')
    print('The Given Equations are: ')
    print_eq(a),print_eq(b)
    check=time.time()
    print('The Product of the two equations are :')
    print_eq(mult(a,b))
    print('Time Consumed is:',time.time()-check)
# worst case is O(n^2) when size of both eq is same and not equal to 1
# best case is O(1) when size is 1 and another ones is 1
# Time Complexity of this Algorithm is O(n)<=y<=O(n^2) (where y is this time complexity) 