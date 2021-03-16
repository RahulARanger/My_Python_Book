import operator
lst1=[int(i) for i in input().split()]
lst2=[int(i) for i in input().split()]
#print(list(map(*,lst1,lst2))) we can't use this * here hence we use the operator functions
print(list(map(operator.mul,lst1,lst2)))