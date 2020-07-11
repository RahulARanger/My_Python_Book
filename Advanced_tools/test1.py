
t = int(input())

while t:
    n = int(input())
    a = list(map(int, input().split()))
    
    if 0 not in a:
        print(0)
    else:
        p = a[a.index(0):]
        print((p.count(0) * 1000) + ((n - a.index(0)) * 100))
    
    t -= 1
            
        