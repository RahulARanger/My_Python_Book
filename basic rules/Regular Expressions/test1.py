import pandas
def diffs(o,t):
    diff=[]
    for i in range(3):
        if t[i]-o[i]==0:pass
        else:
            diff.append(t[i]-o[i])
    return diff        
def factors(o,t):
    factor=[]
    for i in range(3):
        if o[i]!=0:
           if t[i]%o[i]!=0:
               return False,factor
           else:
               if t[i]//o[i]==1:pass
               else:factor.append(t[i]//o[i])
        else:
            return False,factor   
    return True,factor             
def possibilty_1(o,t):
    d=diffs(o,t)
    if len(set(d))<=1:
        return True
    truth,fact=factors(o,t)
    if not truth:return False
    else:
        if len(fact)==0:return True
        else:
            if len(set(fact))==1:return True
    return False        
def add_add(o,t):
    diff=diffs(o,t)
    if len(set(diff))<=2:return True
    return False
def single_factor(a,b):
    if a==0:return False,1
    if b%a==0:
        return True,b//a
    else:
        return False,1        
def add_mult(o,t):
    factors_all=[]
    for i in range(3):
        curr=o[i]
        to=t[i]
        factorz=[]
        for i in range(to-curr+1):
            new_curr=curr+i
            result,fac=single_factor(new_curr,to)
            if result:
                factorz.append((fac,i))
        factors_all+=list(set(factorz))
    for i in factors_all:
        if factors_all.count(i)>1:return True
    return False           
def mult_mult(o,t):
    truth,fa=factors(o,t)
    if not truth:
        return False
    else:
        if len(set(fa))==2:return True    
def single_diff(a,b):
    return b-a
def mult_add(o,t):
    total_diff=[]
    for i in range(3):
        d=[]
        if o[i]==0:
            continue
        else:
            possibiltes=t[i]//o[i]
        loops=possibiltes+1
        for  j in range(1,loops):
            curr=o[i]*j
            differnce=single_diff(curr,t[i])
            d.append((differnce,j))
        #print(d)    
        total_diff+=list(set(d))
    for i in total_diff:
        if total_diff.count(i)>1:return True
    return False  

def possiblitiy_2(o,t):
    if add_add(o,t) or mult_mult(o,t) or add_mult(o,t) or mult_add(o,t):
        return True
    return False
for x in range(int(input())):
    o=[int(i) for i in input().split()]
    t=[int(i) for i in input().split()]
    series=pandas.Series(o,index=t)
    series=series.sort_values()
    o=list(series.values)
    t=list(series.index)
    if possibilty_1(o,t):
        print(1)
        continue
    if possiblitiy_2(o,t):
        print(2)
        continue
    print(3)