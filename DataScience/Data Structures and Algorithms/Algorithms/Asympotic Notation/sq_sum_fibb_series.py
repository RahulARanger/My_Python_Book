# this is the answer for the assignment 7 of the week 2
def create_fibb_series(n):
    c,p=1,1
    ans=[0,1,1]
    for i in range(3,n+1):
        p,c=c,c+p
        ans.append(c**2)
    return ans
series=create_fibb_series(60)
sum_=[]
for n in range(1,61):
    #print(series[:n])
    sum_.append(sum(series[:(n)])%10)
#print(sum_)    
n=int(input())
print(sum_[n%60])
