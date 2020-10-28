
# TODO: Dictionary of list where it's first element is the parent node and second and third is its left and right node

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
    def inorder(self):
        start=self.head
        dup=self.edges.copy()
        switch=True # ? True for searching left node False for right  None for right
        ans=[]
        while True:
            print(ans,start,switch)
            if start is None and switch is None:break
            if switch:
                if dup[start][1] is not  None:
                    start=dup[start][1]
                    switch=True                    
                else:
                    if dup[start][-1] is True:
                        start=dup[start][0]                        
                    else:
                        ans.append(start)  
                        dup[start][-1]=True                  
                    switch=None
            elif switch is None:
                if dup[start][-1] is False:
                    ans.append(start)
                    dup[start][-1]=True
                if dup[start][2] is None:
                    if dup[start][0] is None:
                        break
                    else:
                        start=dup[start][0]
                    switch=None
                else:
                    if dup[dup[start][2]][-1] is True:
                        start=dup[start][0]
                        switch=None
                    else:
                        start=dup[start][2]
                        switch=True
        print(ans)
        return ans
if __name__=='__main__':
    # ! try to insert the elements from the top view
    # ! make sure not to enter the duplicate elements
    '''
    a=Tree(5)
    a.addEdge(5,2,1)
    a.addEdge(5,8,2)
    a.addEdge(2,1,1)
    a.addEdge(2,4,2)
    a.addEdge(8,9,2)
    '''
    a=Tree(4)
    a.addEdge(4,3,1)
    a.addEdge(3,1,1)
    a.addEdge(1,0,1)
    a.addEdge(1,2,2)
    a.addEdge(4,6,2)
    a.addEdge(6,5,1)
    a.addEdge(6,8,2)
    a.addEdge(8,9,2)
    print(a)
    a.inorder()

