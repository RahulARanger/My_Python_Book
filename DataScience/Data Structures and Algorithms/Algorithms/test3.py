def bsearch(lst,key,start=0,end=None):
    if end is None:end=len(lst)-1
    print(lst,start,end)
    if end<start:return -1
    mid=(start+end)//2
    print(mid)
    if key==lst[mid]:return mid
    else:
        return bsearch(lst,key,start,mid-1) if key<lst[mid] else bsearch(lst,key,mid+1,end)
print(bsearch([1,3],2))