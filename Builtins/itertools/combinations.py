import itertools
lst=[int(i) for i in input().split()]
group_size=int(input('Group Size: '))
# order doesn't matter but with duplication is allowed
print(list(itertools.combinations_with_replacement(lst,group_size)))
# order doesn't matter but with no duplication
print(list(itertools.combinations(lst,group_size)))
# order matters
print(list(itertools.permutations(lst,group_size)))