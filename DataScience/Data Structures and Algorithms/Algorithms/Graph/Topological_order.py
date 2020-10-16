from Graph import *
from itertools import *
# This returns only one of the path out of many topically sorted paths.
# ? Refer the example for more understanding
# TODO: order_it() function returns one of the topologically ordered DAG
def combine_lst(lst1,lst2):
    ans=[]
    for i in lst1:
        for j in lst2:
            r=list(i)+list(j)
            ans.append(r)
    return ans


def all_paths(lst,id):
    paths=[]
    dup=lst.copy()
    while True:        
        if len(dup)==0:
            break
        chances=[]
        for i in id:
            if id[i]==0:
                chances.append(i)
        for j in chances:
            for z in dup[j]:
                id[z]-=1
            del dup[j]
            del id[j]
        paths.append(chances)
    print(paths)
    c=[[]]
    for i in range(len(paths)):
        d=permutations(paths[i])
        d=[list(j) for j in d]
        c=combine_lst(c,d)
    return c
def order_it(lst,id):
    check=list(lst.keys())
    ans=[]
    dup=id.copy()
    while True:
        start=None
        for i in check:
            if dup[i]==0:
                start=i
        if start is None:break
        for i in lst[start]:
            dup[i]-=1
        ans.append(start)
        check.remove(start)
    return ans
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
    print(order_it(a.lst,a.inDegree()))
    print(all_paths(a.lst,a.inDegree()))
