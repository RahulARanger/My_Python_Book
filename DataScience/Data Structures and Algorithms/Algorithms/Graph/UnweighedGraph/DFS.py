
# TODO: DFS has lot to do with the grabbing info about the graph
# ? Depth First Search algorithm may return the longest or the shortest path 

'''
Here in this algorithm

when we find the unvisited vertex (adjacent of a node) we immediately explore it before the other adjacent vertices
if it fails then other ... until either stack is empty or the end is found sets this loop to end
'''
class Graph:
    def __init__(self,lst=None):
        self.lst=dict()
        if lst is None:
            pass
        else:
            self.lst=lst
    def find_path(self,start,end):
        self.checklist={}
        for i in self.lst.keys():
            self.checklist[i]=False
        self.checklist[start]=True
        store,extra=(self.explore(start,end))
        if store==False:
            print('No Path Found')
        else:
            print(extra)
    def explore(self,start,end):
        while True:
            q=[]        
            #print(self.checklist,q)
            q.append(start)
            flag=False            
            for i in self.lst[start]:
                if i==end:
                    q.append(i)
                    return True,q
                if self.checklist[i]:
                    pass
                else:
                    flag=True
                    self.checklist[i]=True
                    q.append(i)
                    break   
            if flag:
                store,extra=self.explore(q[-1],end) 
                if store==False:
                    q.pop()
                    if len(q)==0:return False
                    return self.explore(q[-1],end)
                elif store==None:
                    pass
                elif store==True:
                    q.pop()
                    q.extend(extra)
                    return True,q
            else:
                return False,None
    def __str__(self):return str(self.lst)
if __name__=='__main__':
    store={1: [2, 3, 4], 2: [3, 1], 3: [2, 1], 4: [5, 8, 1], 5: [4, 6, 7], 6: [5, 7, 9, 8], 7: [5, 6], 8: [4, 6, 9], 9: [6, 8, 10], 10: [9],11:[12,13]}
    a=Graph(store)
    a.find_path(1,11)
    a.find_path(1,6)
    a.find_path(3,10)        
    a.find_path(4,10)
    print(a)