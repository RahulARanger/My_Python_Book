from Graph import *
def longestpath(lst,id):
    check=[]
    for i in id:
        if id[i]==0:
            check.append(i)
    for i in check:
        start=i
        dup=lst.copy()
        cost={}
        for j in dup.keys():
            cost[i]=0
        cost[start]=1


if __name__=='__main__':
    a=DirectedGraph()
    a.addEdge(1,4)
    a.addEdge(1,3)
    a.addEdge(1,5)
    a.addEdge(5,8)
    a.addEdge(2,8)
    a.addEdge(2,3)
    a.addEdge(4,6)
    a.addEdge(4,8)
    a.addEdge(3,6)
    a.addEdge(6,7)
    a.addEdge(7,8)
    longestpath(a.lst,a.inDegree())