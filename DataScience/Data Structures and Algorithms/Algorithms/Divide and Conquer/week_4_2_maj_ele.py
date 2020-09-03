# This is the answer to the week 4 assignment Question 2
import collections
n=int(input())
lst=[int(i) for i in input().split()]
counts=collections.Counter(lst)
ans=(counts.most_common(1))
if ans[0][1]>len(lst)//2:print(1)
else:print(-1)