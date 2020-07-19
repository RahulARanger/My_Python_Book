import itertools
def n_th_in_series(n):
    prev=0
    present=1
    if n<=2 and n>0:
        return prev if n==1 else present    
    count=2
    for i in itertools.count(0):
        if count==n:return present
        store=present
        present+=prev
        prev=store
        count+=1        
print(n_th_in_series(int(input())+1))