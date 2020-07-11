'''
this is the solution for the question 5 of the week 3 assignment'''
import itertools
def check_this_pair(x,y,a,b):
    if x==a:
        one=a
        if y==b:
            return [one,y]
        else:
            return [one,b]    
    else:
        if x==b:
            return [x,x]
        elif x<b:
            one=x
            if y>=b:
                return [one,b]
            else:
                return [one,y]
    return None                
            
def check(pts):
    i=0
    grps=0
    return_pts=[]
    for count in itertools.count(0):
        limits=pts[i]
        finale=limits[0]
        collected=[pts[i]]
        for j in range(i+1,len(pts)):
            
            limits=check_this_pair(limits[0],limits[1],pts[j][0],pts[j][1])
            if limits is None:
                break
            else:
                finale=limits[0]
                collected.append(pts[j])
        return_pts.append(finale)        
        for __ in collected:
            pts.remove(__)
        grps+=1    
        if len(pts)==0:return grps,return_pts
    return None,None    
n=int(input())
pts=[]
for i in range(n):
    pt=[int(i) for i in input().split()]
    pts.append(pt)
pts.sort()
pts.reverse()
grps,collected=check(pts)    
print(grps)
[print(_,end=' ') for _ in collected]