
# ! This algorithm works for both the directed and the undirected graph

# TODO: Aim is to find the tree from the given graph with minimum cost
import re
class Tree:
    def __init__(self,status):
        self.type=status # True for Directed else Undirected
        self.edges={}
        self.weights={}
    def addEdge(self,a,b,value):
        a,b=str(a),str(b)
        if a in self.edges:
            self.edges[a].append(b)
            self.weights['{}.{}'.format(a,b)]=value
        else:
            self.edges[a]=[b]
            self.weights['{}.{}'.format(a,b)]=value
        if not self.type:
            if b in self.edges:
                self.edges[b].append(a)
            else:
                self.edges[b]=[a]
    def checkCycle(self,a,b):
        a=str(a)
        b=str(b)
        if a not in self.edges:return False
        if b not in self.edges:return False
        stack=[a]
        current=a
        checklist={i:False for i in self.edges}
        checklist[current]=True
        fflag=False
        while True:
            flag=False
            if len(stack)==0:break
            print(stack,self.edges,a,b)
            for i in self.edges[current]:
                if checklist[i]==False:
                    flag=True
                    current=i
                    break
            if not flag:
                stack.pop()
            else:
                if current==b:
                    fflag=True
                    break
                else:
                    stack.append(current)
        return (fflag)
    def __str__(self):
        print(str(self.edges))
        return str(self.weights)
class Graph(Tree):
    def _init__(self,status):
        super().__init__(status)
    def spanTree(self):
        self.tree=Tree(self.type)
        # ? This uses the Kruskal's Algorithm
        dup=sorted(self.weights,key=lambda x:self.weights[x])
        for i in dup:
            edges=re.findall(r'[a-z0-9]+',i)
            print(i)
            if not self.tree.checkCycle(edges[0],edges[1]):
                self.tree.addEdge(edges[0],edges[1],self.weights[i])
            else:
                print('*',i)
        print(self.tree)
    def __str__(self):
        print(str(self.edges))
        return str(self.weights)
if __name__=='__main__':
    a=Graph(False)
    a.addEdge(1,3,18)
    a.addEdge(3,4,70)
    a.addEdge(3,2,6)
    a.addEdge(1,2,10)
    a.addEdge(2,5,20)
    a.addEdge(5,6,10)
    a.addEdge(6,7,5)
    a.addEdge(5,7,10)
    print(a)    
    a.spanTree()