def between(x,y):
    for i in range(x,y+1):
        yield i
x,y=input().split()
x,y=int(x),int(y)
for i in between(x,y):
    print(i,end=' ')        