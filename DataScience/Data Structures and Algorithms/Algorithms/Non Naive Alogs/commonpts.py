
# TODO: The Time Complexity of this Algorithms is O(nlogn) due to sorting else O(n) naive ones is of O(n^2)

# * This problem is similar to finding he common points

# ? Refer this Link: https://www.hackerrank.com/challenges/crush/problem

n,m=[int(i) for i in input().split()]
pairs=0
locstack=[]
stack=[]
for _ in range(m):
    a=[int(i) for i in input().split()]
    stack.append([a[0],'(',a[2]])
    stack.append([a[1],')',a[2]])
stack.sort()
ans=[]
value=0
for i in stack:
    if i[1]=='(':value+=i[2]
    else:
        ans.append(value)
        value-=i[2]
print(max(ans))
