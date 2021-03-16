import itertools
lst=[int(i) for i in input().split()]
#without the group size
print(list(itertools.permutations(lst)))
# with group size
print(list(itertools.permutations(lst,int(input('Enter the Group Size: ')))))