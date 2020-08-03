import collections
def count_sort(lst):
    counts=collections.Counter(lst)
    lst=list(counts.keys())
    lst.sort()
    ans=[]
    for i in lst:
        for j in range(counts[i]):
            ans.append(i)
    return ans  
if __name__=='__main__':
    print(count_sort([int(i) for i in input().split()]))          