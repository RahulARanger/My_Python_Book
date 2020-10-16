
# TODO: This graph is assumed to have the vertices with numerical index and have no value inside it
# TODO: Adjacency list is used
# ? Returns the shortest path between the nodes
'''
1: 2,3
2: 3,1
3: 2,1
4: 5,8
5: 6,7
6: 5,7,8,9
7: 6,5
8: 4,8,6
9: 10
10: 9
11: 12,13
12: 11
13: 11

this is the sample graph with vertices and edges (This is a Undirected Graph)
'''
class Graph:    
    def __init__(self,store=None):
        if store is None:self.lst=dict()
        else:self.lst=store
    def add_edge(self,edge):
        if edge[0] in self.lst.keys():
            pass
        else:
            self.lst[edge[0]]=[]
        self.lst[edge[0]].append(edge[1])
    def print_them(self):
        print(self.lst)
    def find_path(self,start,end):
        path=[]
        apath=[]
        path.append(start)
        checklist={}
        for i in self.lst.keys():checklist[i]=False
        checklist[start]=True
        # Time Complexity is O(m+n) where m is the number of the edges and the n is number of the vetices
        while True:
            queue=[]
            flag=False
            apath.append(start)
            for i in self.lst[start]:
                if not checklist[i]: 
                    if i==end:flag=True                   
                    checklist[i]=True
                    queue.append(i)              
            if len(queue)==0:
                apath.pop()
                del path[path.index(start)]
                if len(path)==0:break
                start=path[-1]  
            else:
                start=queue[0]
                path.extend(queue)   
            if flag:break
        if flag:apath.append(end)
        else:
            print('Not Possible')
            return None
        print(apath)
    def __str__(self):return str(self.lst)
if __name__=='__main__':
    store={1: [2, 3, 4], 2: [3, 1], 3: [2, 1], 4: [5, 8, 1], 5: [4, 6, 7], 6: [5, 7, 9, 8], 7: [5, 6], 8: [4, 6, 9], 9: [6, 8, 10], 10: [9],11:[12,13]}
    a=Graph(store)
    n=int(input('Enter  the Number of edges: '))
    a.find_path(1,11)
    a.find_path(1,6)
    a.find_path(3,10)    
    a.find_path(1,6)
    print(a)
