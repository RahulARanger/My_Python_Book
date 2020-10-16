
# TODO: To know the Working of the Bell man ford algorithm refer : 

# ? Bellman ford algorithm does the same job as the dijkstra's algorithm
# ? But it will also do the same thing even for the negative weighted graphs (in which dijkstra's algo. failed)

try:
    from weighedgraph import *
except:
    from WeighedGraph.ShortestPaths.weighedgraph import *
class BellManFordAlgo:
    def __init__(self,status):
        self.graph=UndirectedGraph() if status else DirectedGraph()        
    def addEdge(self,a,b,data):
        self.graph.addEdge(a,b,data)
    def __str__(self):
        print(str(self.graph.values))
        return str(self.graph.lst)
    def shortestPath(self,start):
        self.dvalues={}
        dup=self.graph.lst.copy()
        for i in dup.keys():
            self.dvalues[i]=None
        self.dvalues[start]=0
        self.keyorder=[]
        for i in dup.keys():
            pairs=[]
            for j in dup[i]:
                pairs.append((i,j))
            if len(pairs)>0:self.keyorder.extend(pairs)
        print(self.keyorder)
        for i in range(len(dup.keys())-1):
            for j in self.keyorder:
                if self.dvalues[j[0]] is None:pass
                else:
                    e=self.graph.values[j[0]][j[1]]+self.dvalues[j[0]]
                    if self.dvalues[j[1]] is None:
                        self.dvalues[j[1]]=e
                    else:
                        print(j,e,self.dvalues[j[1]],self.graph.values[j[0]][j[1]])
                        if e<self.dvalues[j[1]]:
                            self.dvalues[j[1]]=e
            print(self.dvalues)
if __name__=='__main__':
    a=BellManFordAlgo(False)    
    '''
    Test Case 1
    a.addEdge('A','B',6)
    a.addEdge('C','B',-2)
    a.addEdge('A','D',5)
    a.addEdge('A','C',4)
    a.addEdge('D','C',-2)
    a.addEdge('B','E',-1)
    a.addEdge('C','E',3)
    a.addEdge('E','F',3)
    a.addEdge('D','F',-1)'''
    a.addEdge(1,8,8)
    a.addEdge(8,7,1)
    a.addEdge(7,6,-1)
    a.addEdge(5,6,-1)
    a.addEdge(4,5,3)
    a.addEdge(3,4,1)
    a.addEdge(3,2,1)
    a.addEdge(1,2,10)
    a.addEdge(2,6,2)
    a.addEdge(7,2,-4)
    a.addEdge(6,3,-2)
    print(a.graph.lst)
    a.shortestPath(1)
    
