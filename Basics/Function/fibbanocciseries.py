x=int(input())
curr,next=0,1
for i in range(x):
    print(str(curr)+' ',end='')
    next+=curr
    a=next
    next=curr
    curr=a    