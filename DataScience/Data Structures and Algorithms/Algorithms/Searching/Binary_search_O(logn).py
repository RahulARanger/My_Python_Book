def bs(lst,s,e,x):
    mid=(s+e)//2
    if lst[mid]==x:return mid
    if s>e:return -1
    if lst[mid]>x:return bs(lst,s,mid-1,x)
    else:return bs(lst,mid+1,e,x)
if __name__=='__main__':
    a=[int(i) for i in input('Enter the List of Numbers: ').split()]
    a.sort()
    note=(bs(a,0,len(a)-1,int(input('Enter the element to search: '))))
    if note==-1:print('NOT_FOUND')
    else:print('Found at:',note+1)