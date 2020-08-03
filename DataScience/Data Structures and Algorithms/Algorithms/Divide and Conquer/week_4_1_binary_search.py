# This is the answer to the week4 assignment question1 
def bs(lst,start,end,k):
    mid=start+end
    mid//=2
    if start>end:return -1
    if start==end-1:
        if lst[start]==k:return start
        elif lst[end]==k:return end
        else:return -1
    if lst[mid]==k:return mid
    if lst[mid]>k:return bs(lst,start,mid-1,k)
    else:return bs(lst,mid+1,end,k)

a=[int(i) for i in input().split()]
a=a[1:]
a.sort()
b=[int(i) for i in input().split()]
b=b[1:]
for i in b:
    print(bs(a,0,len(a)-1,i),end=' ')