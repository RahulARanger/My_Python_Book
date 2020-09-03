def bs(lst,key,start=0,end=None):
    if end is None:end=len(lst)-1
    if start>end:return -1
    mid=(start+end)//2
    if lst[mid]==key:return mid
    else:
        return bs(lst,key,start,mid-1) if lst[mid]>key else bs(lst,key,mid+1,end)
lst=[int(i) for i in input('Enter Some Numbers (in ascending order): ').split()]
lst.sort()
k=int(input('Enter a Number to search: '))
ans=bs(lst,k)
if ans!=-1: print('Element is Found at: {}'.format(ans))
else: print('Not Present')
# ?  The Time Complexity of the Binary Algorithm is O(log(n))