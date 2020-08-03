def quick_sort(lst,start,end):
    length=end-start+1
    if length<=1:return
    else:
        pivot=start
        left=pivot+1
        right=end
        flag=True
        
        while right>=left:
            if flag and lst[left]<=lst[pivot]:
                left+=1
                if left>=length:break
            elif lst[pivot]<lst[left]:flag=False
            if not flag and lst[right]>=lst[pivot]:
                right-=1
            elif lst[right]<lst[pivot]:
                flag=True
                if left>=length:break
                lst[left],lst[right]=lst[right],lst[left]
        lst[pivot],lst[right]=lst[right],lst[pivot]   
        quick_sort(lst,start,right-1)
        quick_sort(lst,right+1,end)
if __name__=='__main__':
    lst=[int(i) for i in input().split()]
    quick_sort(lst,0,len(lst)-1)
    print(lst)
