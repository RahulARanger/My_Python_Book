
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
    def maximum(self):
        # * Time Complexity is prop. to height of the tree
        start=self.head
        store=None
        while True:
            print('*',start)
            if self.edges[start][2] is None:
                store=start
                break
            else:
                start=self.edges[start][2]
        return store

if __name__ == "__main__":
    a=Tree(5)
    a.addEdge(5,3,1)
    a.addEdge(5,7,2)
    a.addEdge(3,1,1)
    a.addEdge(1,2,2)
    a.addEdge(3,4,2)
    a.addEdge(7,9,2)
    a.addEdge(9,8,1)
    print(a.maximum())
