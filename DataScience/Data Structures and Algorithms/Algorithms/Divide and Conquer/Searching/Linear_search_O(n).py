def ls(lst,k,n,now):
    if lst[now]==k:return now+1
    elif now==n-1:return -1;
    else:return ls(lst,k,n,now+1)
lst=[int(i) for i in input('Enter some Numbers in List: ').split()]    
k=int(input('Enter the Number to Search from: '))
ans=ls(lst,k,len(lst),0)
if ans==-1:print('NOT_FOUND')
else:print(ans)

# Time Complexity:
            # worst-case: O(n) Best-case: O(1)