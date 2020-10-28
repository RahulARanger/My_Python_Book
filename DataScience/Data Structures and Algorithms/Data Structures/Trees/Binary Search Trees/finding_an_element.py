class Tree:
    def __init__(self,head):
        self.edges={head:[None,None,None,False]}
        self.head=head
    def addEdge(self,a,b,mode): # ? manual insertion
        self.edges[b]=[None,None,None,False]
        if mode==1:
            self.edges[a][1]=b
        else:
            self.edges[a][2]=b
        self.edges[b][0]=a
    def __str__(self):
        return str(self.edges)
    def find(self,element):
        start=self.head
        dup=self.edges.copy()
        while True:
            print(start)
            if start is None:return False
            if start==element:
                return True
            else:
                if start>element:
                    start=dup[start][1]
                else: 
                    start=dup[start][2]
if __name__=='__main__':
    a=Tree(4)
    a.addEdge(4,3,1)
    a.addEdge(3,1,1)
    a.addEdge(1,0,1)
    a.addEdge(1,2,2)
    a.addEdge(4,6,2)
    a.addEdge(6,5,1)
    a.addEdge(6,8,2)
    a.addEdge(8,9,2)
    print(a.find(8))
    print(a.find(7))