def dist(pt1,pt2):
    x1,y1=pt1
    x2,y2=pt2
    return ((abs(y2-y1)**2)+(abs(x2-x1)**2))**0.5

def two_pointer(pts):
    pair=[]
    check=None
    for i in range(2):
        for j in range(i+1,3):
            if check is None:
                pair=[pts[i],pts[j]]
                check=dist(pts[i],pts[j])
            else:
                test=dist(pts[i],pts[j])
                if check>=test:
                    pair=[pts[i],pts[j]]
                    check=test
    return pair

if __name__=='__main__':
    n=int(input())
    pts=[]
    for i in range(n):
        pt=[int(j) for j in input().split()]
        pts.append(pt)
    pts_x=sorted(pts,key=lambda x:x[0])
    
'''‎
11    
4 4
-2 -2
-3 -4
-1 3
2 3
-4 0
1 1
-1 -1
3 -1
-4 2
-2 4
'''