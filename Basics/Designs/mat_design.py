# enter row and column to proceed
n,m=input().split()
n,m=int(n),int(m)
mid=int((n+1)/2)
series_length=mid-1
odd,three_mult=[],[]
for i in range(series_length):
    odd.append(2*i+1)
for i in range(series_length):
    three_mult.append(3*(i+1))
three_mult.reverse()
design='.|.'
adjust=0
for i in range(n):
        if i+1==mid:
            print('{:-^{}}'.format('WELCOME',m),end='')
            three_mult.reverse()
            odd.reverse()
            adjust=mid            
        else:
            for g in range(three_mult[i-adjust]):
                print('-',end='')
            for g in range(odd[i-adjust]):
                print(design,end='')
            for g in range(three_mult[i-adjust]):
                print('-',end='')
        print()