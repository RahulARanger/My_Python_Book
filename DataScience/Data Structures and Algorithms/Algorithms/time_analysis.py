def check_slope(pt1,pt2):
    x1,y1=pt1
    x2,y2=pt2
    if y2==y1 or x2==x1:return True
    else: return False
def check_this(lst,pt):
    for i in lst:
        if check_slope(i,pt):
            return True
    return False      
def missing_pt(pts):
    pts.sort()
    pt1,pt2,pt3=pts
    #print(pts)
    if pt1[0]==pt2[0] and pt1[1]==pt3[1]:
        #print('a')
        return pt3[0],pt2[1]
    elif pt1[1]==pt2[1] and pt1[0]!=pt3[0] and pt1[0]!=pt3[1]:
        #print('b')
        return pt1[0],pt3[1]
    elif pt1[0]==pt2[0] and pt1[0]!=pt3[0] and pt1[0]!=pt3[1]:
        #print('c')
        return pt3[0],pt1[1]
    else:
        #print('d')
        return pt1[0],pt2[1]
for _ in range(int(input())):
    n=int(input())
    r=4*n-1
    pts=None
    on_hold=[]
    for i in range(r):
        pt=[int(i) for i in input().split()]
        if pts is None:
            pts=[]
            pts.append(pt)
        else:
            if check_this(pts,pt):
                pts.append(pt)
            else:
                on_hold.append(pt)    
            if len(pts)==2 or len(pts)==3:
                for i in on_hold:
                    if check_this(pts,i):
                        pts.append(i)
            if len(pts)==4:
                pts=None
    print(pts)
    x,y=missing_pt(pts)
    print(x,y)
    #check that this format 

               ##########
               ##########
               ##########
    #####################
    ###########
    ###########