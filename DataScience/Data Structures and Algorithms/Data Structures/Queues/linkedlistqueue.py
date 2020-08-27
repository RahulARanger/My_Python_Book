class Node:
    index=0
    def __init__(self,data=None):
        self.data=None
        self.address=None
    def enqeue(self,data):
        if Node.index==0:
            self.data=data
        else:
            check=self
            while check.address is not None:
                check=check.address
            new=Node()
            new.data=data
            check.address=new
        Node.index+=1 
    def deque(self):
        if Node.index==0 or Node.index==1:
            self.data,self.address=None
            print('Queue Underflow')
        else:
            check=self
            check.data=check.address.data
            check.address=check.address.address
            Node.index-=1
    def __str__(self):
        check=self
        collect=str()
        collect=str(check.data)+' '
        for i in range(Node.index-1):
            check=check.address
            collect+=str(check.data)+' '
        return collect 
if __name__=='__main__':
    a=Node()
    for i in range(1,7):
        a.enqeue(i)
    print(a)
    a.deque()
    a.deque()
    a.deque()
    a.deque()
    print(a)
    a.deque()
    print(a)
