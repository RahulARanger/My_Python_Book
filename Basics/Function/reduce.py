from functools import *
a=input().split()
a=[int(i) for i in a]
result=reduce(lambda x,y:x+y,a)
print(result)