
# TODO: Distribute N black balls among 10 boxes so that every two boxes have different number of balls (you can put 0 balls in some box if you want to). Fill in numbers of black balls in each box below.
n=int(input())
lst=[]
if n>=45:
    lst.append(0)
    for i in range(8):
        lst.append(i+1)
        n-=i+1
    lst.append(n)    
    [print(_,end=' ') for _ in lst]
else:
    print('Not Possible')
# * refer this for more details: https://www.coursera.org/learn/what-is-a-proof/gradedLti/6rSSw/puzzle-balls-in-boxes