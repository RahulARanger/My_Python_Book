
# ? sounds suprising we can actually sort and work on this which is better than the naive algo.

# This is the answer to the week 4 assignment Question 2
n=int(input())
lst=[int(i) for i in input().split()]
lst.sort()
big=1
track=1
for i in range(len(lst)-1):
    if lst[i]==lst[i+1]:
        track+=1
    else:
        if track>big:big=track
        track=1
if track>big:big=track
print(1 if big>len(lst)//2 else 0)