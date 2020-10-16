
class Tree:
    def __init__(self):
        self.lst={}
        self.weights={}
    def addEdge(self,a,b,value):
        a,b=str(a),str(b)
        if a in self.lst.keys():
            self.lst[a].append(b)
        else:
            self.lst[a]=[b]
        if b in self.lst.keys():
            self.lst[b].append(a)
        else:
            self.lst[b]=[a]
        self.weights['{}.{}'.format(a,b)]=value
        self.weights['{}.{}'.format(b,a)]=value
    def __str__(self):
        print(str(self.lst))
        return str(self.weights)
class Graph(Tree):
    def __init__(self):
        super().__init__()
    def primalgo(self):
        checklist={}
        for i in self.lst.keys():checklist[i]=False
        a=list(self.lst.keys())[0]
        customized={}
        for i in self.lst.keys():customized[i]=[None,None]
        checklist[a]=True
        start=a
        stack=[a]
        while True:
            
            neighbors=self.lst[start]
            check,index=None,None
            for i in neighbors:
                if checklist[i]==False:
                    e=self.weights['{}.{}'.format(start,i)]                    
                    if customized[i][0] is None:
                        customized[i]=[e,start]
                    else:
                        if customized[i][0]>e:
                            customized[i]=[e,start]
                    stack.append(i)
            del stack[stack.index(start)]            
            checklist[start]=True
            if len(stack)==0:break
            check,index=None,None
            stack=list(set(stack))
            for i in stack:
                e=customized[i][0]
                if check is None:
                    check=e
                    index=i
                else:
                    if check>e:
                        check=e
                        index=i
            start=index
        self.Tree=Tree()
        for i in customized:
            if customized[i][0] is None:continue
            else:
                self.Tree.addEdge(i,customized[i][1],customized[i][0])
        return self.Tree

if __name__=='__main__':
    a=Graph()
    a.addEdge(1,3,18)
    a.addEdge(3,4,70)
    a.addEdge(3,2,6)
    a.addEdge(1,2,10)
    a.addEdge(2,5,20)
    a.addEdge(5,6,10)
    a.addEdge(6,7,5)
    a.addEdge(5,7,10)
    print(a)    
    print('***'*66)
    print(a.primalgo())
