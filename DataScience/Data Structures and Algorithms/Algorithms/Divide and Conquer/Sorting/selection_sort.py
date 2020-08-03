def bub_sort(lst):
    lst_=lst.copy()
    ans=[]
    for i in range(len(lst_)):
        mini=None
        for j in lst_:
            if mini is None:mini=j
            else:mini=j if j<mini else mini
        ans.append(mini)
        lst_.remove(mini)
    return ans    
if __name__=='__main__':    
    lst=[int(i) for i in input().split()]
    print('The Sorted list of {} is: {}'.format(lst,bub_sort(lst)))

# the time complexity of Selection Sort is O(n^2)