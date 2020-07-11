for _ in range(int(input())):
    g=int(input())
    for __ in range(g):
        i,n,q=[int(i) for i in input().split()]
        mid=n//2
        if n%2==0:
            coins=[mid,mid]
        else:
            coins=[mid,mid+1]
        if i==2:
            coins.reverse()
            print(coins[q-1])
        
        else:
            print(coins[q-1])

