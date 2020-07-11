def alpha_part(alpha,start,length):
    mid=int(length/2)+1
    for i in range(mid-1):
        print(alpha[start],end='')
        start-=1
    print(alpha[start],end='')
    start+=1
    for i in range(mid-1):
        print(alpha[start],end='')
        start+=1
def palpha_part(alpha,start,length):
    adjust=0
    mid=int(length/2)+1
    for i in range(mid-1):
        print(alpha[start],end='-')
        start-=1
    if length<=1:print(alpha[start],end='')
    else:print(alpha[start],end='-')
    start+=1
    for i in range(mid-1):
        if i==mid-2:
            print(alpha[start],end='')
            break
        print(alpha[start],end='-')
        start+=1        
n=int(input())
total=n*2-1
alphas='abcdefghijklmnopqrstuvwxyz'
palpha=[str(i) for i in alphas]
alpha=['-'+str(i) for i in alphas]
#print(alpha)
mid=int((total+1)/2)
size=mid-1
two_mult,odd,index=[],[],None
index=size
for i in range(size):
    two_mult.append(int(2*(i+1)))
for i in range(size):
    odd.append(2*i+1)
two_mult.reverse()    
for i in range(size):
    for j in range(two_mult[i]-1):print('-',end='')
    #print(index,odd[i])
    alpha_part(alpha,index,odd[i])
    for j in range(two_mult[i]):print('-',end='')
    print()
odd.reverse()
two_mult.reverse()
palpha_part(palpha,index,size*2)
print()
for i in range(size):
    for j in range(two_mult[i]-1):print('-',end='')
    #print(index,odd[i])
    alpha_part(alpha,index,odd[i])
    for j in range(two_mult[i]):print('-',end='')
    print()    
 
