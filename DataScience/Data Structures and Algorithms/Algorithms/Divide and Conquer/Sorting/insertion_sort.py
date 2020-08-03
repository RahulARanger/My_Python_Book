def insert_sort(lst):
    for i in range(len(lst)):
        note=i
        for j in range(0,i):
            if lst[note]<lst[j]:
                insert=lst[note]
                del lst[note]
                lst.insert(j,insert)
                note=j
                break
if __name__=='__main__':       
    lst=[int(i) for i in input().split()]
    insert_sort(lst)
    print(lst)
# This is Actually Improved form of some Soting Algorithm Called bubble Sort
# Time Complexity of Insertion Sort is O(n^2).
# insertion sort is better than the selection sort in terms of both time and space consumed