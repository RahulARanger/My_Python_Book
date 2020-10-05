
# ? I personally feel quick sort isn't better than the merge sort so i will either use timsort (sorted() or.sort()) or merge sort

if __name__=='__main__':
    n=int(input())
    lst=[int(i) for i in input().split()]
    lst.sort()
    for i in lst:
        print(i,end=' ')
