def merge(lst,lst2):
    ans=[]
    index_1,index_2=0,0
    for  i in range(len(lst)+len(lst2)):
        if index_1==len(lst):
            ans.append(lst2[index_2])
            index_2+=1
            continue
        if index_2==len(lst2):
            ans.append(lst[index_1])    
            index_1+=1
            continue
        if lst[index_1]<lst2[index_2]:
            ans.append(lst[index_1])
            index_1+=1
        else:
            ans.append(lst2[index_2])
            index_2+=1 
    return ans    
def mersort(lst):
    length=len(lst)
    if length>2:
        mid=length//2
        left=lst[:mid]
        right=lst[mid:]
        left=mersort(left)
        right=mersort(right)
        lst=merge(left,right)
    else:
        if length==2:
            if lst[0]>lst[1]:lst[1],lst[0]=lst[0],lst[1]
    return lst
if __name__=='__main__':
    lst=[int(i) for i in input().split()]
    print(mersort(lst))
    
# Time Complexity of the Merge Sort is O(nlog(n))    