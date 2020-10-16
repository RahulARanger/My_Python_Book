class UndirectedGraph:
    def __init__(self,lst=None):
        self.lst=dict()
        if lst is not None:
            self.lst.update(lst)
    def addEdge(self,a,b):
        if a in self.lst.keys():
            self.lst[a].append(b)
        else:
            self.lst[a]=[b]
        if b in self.lst.keys():
            self.lst[b].append(b)
        else:
            self.lst[b]=[a]        
    def __str__(self):return str(self.lst)
class DirectedGraph:
    def __init__(self,lst=None):
        self.lst=dict()
        if lst is not None:
            self.lst.update(lst)
    def addEdge(self,a,b):
        if b not in self.lst.keys():
            self.lst[b]=[]
        if a in self.lst.keys():
            self.lst[a].append(b)
        else:
            self.lst[a]=[b]
    def inDegree(self):
        self.id={}
        for i in self.lst.keys():
            self.id[i]=0
        for i in self.lst.keys():
            for j in self.lst[i]:
                self.id[j]+=1
        return self.id


    def __str__(self):return str(self.lst)
