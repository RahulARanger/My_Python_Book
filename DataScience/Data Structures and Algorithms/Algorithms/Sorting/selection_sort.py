def ssort(lst):
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]>lst[j]:lst[j],lst[i]=lst[i],lst[j]
    return lst
if __name__=='__main__':
    lst=[int(i) for i in input('Enter the Numbers: ').split()]
    print(ssort(lst))