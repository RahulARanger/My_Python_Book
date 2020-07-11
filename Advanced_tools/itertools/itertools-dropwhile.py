import itertools
lst=[int(i) for i in input().split()]
print(list(itertools.dropwhile(lambda x: True if x%2==0 else False,lst)))