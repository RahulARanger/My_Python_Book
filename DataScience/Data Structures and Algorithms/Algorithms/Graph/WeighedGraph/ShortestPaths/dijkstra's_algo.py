
# ? Make sure to follow the entire process
# TODO: for video reference: https://www.youtube.com/watch?v=smHnz2RHJBY&t=1107s
try:
    from weighedgraph import *
except:
    from WeighedGraph.ShortestPaths.weighedgraph import *
# ? False for Directed else Undirected Graph
class DijkstraAlgo:
    def __init__(self,status):
        self.graph=UndirectedGraph() if status else DirectedGraph()
    def addEdge(self,a,b,data):
        self.graph.addEdge(a,b,data)
    def __str__(self):
        print(str(self.graph.values))
        return str(self.graph.lst)
    
    def shortestPath(self,starte,ende):
        end=ende
        start=starte
        self.dup=self.graph.lst.copy()
        print(self.dup)
        self.note={}
        self.log=[]
        for i in self.dup.keys():
            if i==start:self.note[start]=0
            else:self.note[i]=None
        self.log.append(self.note.copy())
        while True:
            print(self.log,'%')
            if start==ende:break
            neighbours=self.dup[start]
            for i in neighbours:
                if i not in self.dup.keys():
                    continue
                a=self.note[start]+self.graph.values[start][i]
                if self.note[i] is None:
                    self.note[i]=a
                else:
                    if self.note[i]>a:
                        self.note[i]=a
            del self.dup[start]
            del self.note[start]
            if len(self.dup)==0:
                print('No possile paths are available')
                break
            index=None
            for i in self.note.keys():
                if index is None:
                    index=i
                else:
                    if self.note[i] is not None:
                        if self.note[index]>self.note[i]:
                            index=i
            start=index
            self.log.append(self.note.copy())
        stack=[]
        index=len(self.log)-1
        for i in range(len(self.log)):
            if end not in self.log[i].keys():
                index=i-1
        print(self.log)
        stack.append(end)
        while True:
            check=index-1
            if check<0:
                break
            print(stack,end,index,check,self.log[index][end],self.log[check][end])
            flag=False
            if self.log[check][end] is None:flag=True
            else:
                if self.log[index][end]<self.log[check][end]:flag=True
            if flag:
                where=None
                for i in self.log[check]:
                    if self.log[check][i] is not None:
                        if where is None:where=i
                        else:
                            if self.log[check][where]>self.log[check][i]:where=i
                stack.append(where)
                end=where
            else:
                pass
            index-=1
        return ''.join(list(reversed(stack)))
if __name__=='__main__':
    a=DijkstraAlgo(False)
    a.addEdge('A','B',10)
    a.addEdge('B','D',1)
    a.addEdge('E','D',6)
    a.addEdge('E','A',2)
    a.addEdge('C','B',3)
    a.addEdge('A','C',5)
    a.addEdge('C','E',2)
    a.addEdge('C','D',9)
    print(a.shortestPath('A','B'))
    
