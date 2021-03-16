import itertools
lst=list(itertools.repeat(25,6))
print(lst)
lst=list(itertools.repeat('ab',6))
# repeats the 'ab' six times inside the list it's like ['ab']*6
print(lst)