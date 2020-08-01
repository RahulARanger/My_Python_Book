def bs(lst,k,start,end):
    print(start,end)
    index=(start+end)//2
    if start>end:return False,len(lst)-1
    if start==end-1:
        if k==lst[start]:return True,start
        elif k==lst[end]:return True,end
        else:return False,start
    if lst[index]==k:return True,index
    elif lst[index]>k:return bs(lst,k,start,index-1)
    elif lst[index]<k:return bs(lst,k,index+1,end)
lst=[int(i) for i in input('Enter Some Numbers: ').split()]
lst.sort()
k=int(input('Enter a Number to search: '))
res,ans=bs(lst,k,0,len(lst)-1)
if res:
    print('The Element is present at the Index: ',ans+1)
else:
    print('The given element is not present in the list\n')
    print('We can insert the new element at the index: ',ans+1)    

    # The Time Complexity of the Binary Algorithm is O(log(n))