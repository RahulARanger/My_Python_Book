def sum_(lst):
    s=0
    for i in lst:s+=i
    return s
def max_(lst):
    m=lst[0]
    index=0
    for i in range(1,len(lst)):
        if m<lst[i]:
            m=lst[i]
            index=i
    del lst[index]    
    return m
lst=[int(i) for i in input().split()]
x=int(input())
sub=[]
for i in range(len(lst)):
    sub.append(max_(lst))
    if sum_(sub)>x:
        print(sub)
        break