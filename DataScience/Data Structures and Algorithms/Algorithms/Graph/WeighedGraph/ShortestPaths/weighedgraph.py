class UndirectedGraph:
    def __init__(self):
        self.lst=dict()
        self.values=dict()
    def addEdge(self,a,b,value):
        insert={b:value}
        insert1={a:value}
        if a in self.lst.keys():
            self.lst[a].append(b)
            self.values[a].update(insert)
        else:
            self.lst[a]=[b]
            self.values[a]=insert
        if b  in self.lst.keys():
            self.lst[b].append(a)
            self.values[b].update(insert1)
        else:
            self.lst[b]=[a]
            self.values[b]=insert1
    def __str__(self):
        print(str(self.lst))
        return str(self.values)
class DirectedGraph:
    def __init__(self):
        self.lst=dict()
        self.values=dict()
    def addEdge(self,a,b,value):
        insert={b:value}
        if a in self.lst.keys():
            self.lst[a].append(b)
            
            self.values[a].update(insert)
        else:
            self.lst[a]=[b]
            self.values[a]=insert
        if b  not in self.lst.keys():
            self.lst[b]=[]
            self.values[b]={}
    def __str__(self):
        print(str(self.lst))
        return str(self.values)
if __name__=='__main__':
    a=UndirectedGraph()
    a.addEdge(3,4,70)
    a.addEdge(3,2,6)
    a.addEdge(3,1,80)
    a.addEdge(2,5,20)
    a.addEdge(1,2,10)
    a.addEdge(5,6,50)
    a.addEdge(5,7,10)
    a.addEdge(6,7,5)
    print(a.values[5][6]) # this would be 50
    print(a)
