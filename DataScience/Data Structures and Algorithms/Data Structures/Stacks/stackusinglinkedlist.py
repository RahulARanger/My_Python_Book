class Node:
    index=0
    def __init__(self):
        self.data=None
        self.address=None
    def append(self,data):
        check=self
        if Node.index==0:
            self.data=data
        else:
            for i in range(Node.index-1):
                check=check.address
            new=Node()
            new.data=data
            check.address=new
        Node.index+=1
    def pop(self):
        if Node.index==0:
            print('Stack Underflow') 
            return None
        check=self
        if Node.index==1:check.data=None
        for i in range(Node.index-2):
            check=check.address
        check.address=None
        Node.index-=1
    def __str__(self):
        combine=' '
        check=self
        combine+=str(check.data)+' '
        for i in range(Node.index-1):
            check=check.address
            combine+=str(check.data)+' '
        return combine
if __name__=='__main__':
    a=Node()
    a.append(1)
    a.append(2)
    a.append(3)
    print(a)
    a.pop()
    print(a)
    a.pop()
    print(a)
    a.pop()
    print(a)
    a.pop()
    a.append(1)
    print(a)
