
# TODO: Modified binary insertion sort 
def bsearch(lst,s,e,x):
    mid=(s+e)//2
    if mid==-1:return 0
    if s>e:return len(lst)
    if lst[mid]>x:return bsearch(lst,s,mid-1,x)
    elif lst[mid]<x:return bsearch(lst,mid+1,e,x)
    return mid
def isort(lst):
    ans=[]
    for i in lst:
        where=bsearch(ans,0,len(ans)-1,i)
        ans.insert(where,i)
    return ans
if __name__=='__main__':
    a=[int(i) for i in input('Enter the Numbers: ').split()]
    print(isort(a))