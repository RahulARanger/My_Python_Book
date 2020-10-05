
'''
    ?  Most of the problems which can be solved by divide and conquer can be done through merge sort way

problem: Find the pairs in list where i<j but a[i]>a[j] where a is the list
'''
# ? we can use merge sort algorithm to solve such problems
pairs=0
def merge(lst,lst2):
    ans=[]
    re=len(lst)
    global pairs
    index_1,index_2=0,0
    for  i in range(len(lst)+len(lst2)):
        if index_1==len(lst):
            ans.append(lst2[index_2])
            index_2+=1
            continue
        if index_2==len(lst2):
            ans.append(lst[index_1])    
            index_1+=1
            re-=1
            continue
        if lst[index_1]<=lst2[index_2]:
            ans.append(lst[index_1])
            index_1+=1
            re-=1
        else:
            pairs+=re
            #print(lst2,lst,re)
            ans.append(lst2[index_2])
            index_2+=1 
    return ans    
def mersort(lst):
    global pairs
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
            if lst[0]>lst[1]:
                pairs+=1
                lst[1],lst[0]=lst[0],lst[1]
    return lst
n=int(input())
lst=[int(i) for i in input().split()]
mersort(lst)
print(pairs)