for i in range(int(input())):
    n=int(input())
    payment=0
    months=input().split()
    months=list(map(lambda x:int(x),months))
    for i in range(len(months)):
        if months[i]==0:
            if 1 in months[i:]:
                index=months.index(1,i)
                months[index]=0
                payment+=100
            else:payment+=1100
    print(payment)      
    