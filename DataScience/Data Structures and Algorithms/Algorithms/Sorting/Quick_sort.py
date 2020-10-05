def qsort(lst,s,e):
    len=(e-s)+1    
    if len<=1:
        return None    
    print(lst)
    pp=s
    sp=s+1
    ep=e
    flag=True
    while True:        
        print(sp,ep,pp,flag)
        if sp>ep: 
            lst[ep],lst[pp]=lst[pp],lst[ep]
            pp=ep
            break
        if flag:
            if lst[pp]>=lst[sp]:
                sp+=1
            else:
                flag=False
        else: 
            if lst[pp]<=lst[ep]:
                ep-=1
            else:
                lst[ep],lst[sp]=lst[sp],lst[ep]                
                flag=True
    print(pp,s,e)
    if pp-1>=0:
        print(pp)
        qsort(lst,s,pp-1)
    if pp+1<=e:
        print(pp+1)
        qsort(lst,pp+1,e)
if __name__=='__main__':
    a=[int(i) for i in input('Enter the Numbers: ').split()]
    qsort(a,0,len(a)-1)
    print(a)