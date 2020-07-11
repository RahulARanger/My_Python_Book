'''
problem statement:

u are given a weights and calories of the food items so try to pick them in a way they fit in N kg capacity of knapsack 
and their values are a s high as possible

problem statement: https://practice.geeksforgeeks.org/problems/fractional-knapsack/0

'''
for _ in range(int(input())):
    n,w=[float(i) for i in input().split()]
    lst=[float(i) for i in input().split()]
    pairs=[(x/y,x,y) for x,y in zip(lst[0:len(lst):2],lst[1:len(lst):2])]
    pairs.sort()
    pairs.reverse()
    collected=0
    for i in pairs:
        if w==0:
            break
        if w>=i[2]:
            collected+=i[1]
            w-=i[2]
        else:
            remaining=w/i[2]
            collected+=i[1]*remaining
            w=0
    print('{:.2f}'.format(collected))        



