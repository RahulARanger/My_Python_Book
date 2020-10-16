
# ! try to excute from the Graph Directory
from Graph import *
def check(lst):    
    checklist=dict()
    for i in lst:
        checklist[i]=False
    count=0    
    while True:
        flag=True
        start=None
        for i in checklist:
            if checklist[i]==False:
                start=i
                flag=True
                break
            else:
                flag=False
        if not flag:break
        checklist[start]=True
        # print(lst)
        # print(start,'&')
        explore(lst,start,checklist)
        # print(checklist,'#')
        count+=1
    if count>1:
        print('Disconnected Graph with {} connected parts'.format(count))
    else:
        print('Connected Graph')
def explore(lst,start,checklist):
    q=[]
    q.append(start)
    while True:
        flag=True
        # print(checklist)
        for i in lst[start]:
            if checklist[i]:
                pass
            else:
                flag=False
                checklist[i]=True
                q.append(i)
                break
        if not flag:
            # print(q)
            note=explore(lst,q[-1],checklist)
            if note is False:
                q.pop()
            if len(q)==0:break
        else:
            # print(q)
            return False        

if __name__=="__main__": 
    a=UndirectedGraph()
    a.addEdge(1,2)
    a.addEdge(1,5)
    a.addEdge(6,6)
    a.addEdge(5,9)
    a.addEdge(9,10)
    a.addEdge(3,4)
    a.addEdge(3,7)
    a.addEdge(3,8)
    a.addEdge(8,12)
    a.addEdge(7,11)
    check(a.lst)
    print(a)

