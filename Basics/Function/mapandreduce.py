from functools import *
lists=[int(i) for i in input().split()]
lists=list(map(lambda x:x*x,lists))
lists=reduce(lambda x,y:x+y,lists)
print(lists)