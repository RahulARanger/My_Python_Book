class Node:
    index=0
# * Transversal process
    def __str__(self):
        check=self
        combine=''        
        combine+=str(check.data)+ ' '
        for i in range(Node.index-1):
            check=check.address
            combine+=str(check.data)+ ' '
        return combine
# ! Searching process (linear search)
    def search(self,value):
        check=self
        if value==check.data:return 1
        for i in range(Node.index-1):
            check=check.address
            if value==check.data:return i+1
        return -1    
# !Inserting elements at the end
    def append(self,data):
        check=self
        if Node.index==0:
            check.data=data
        else:
            new=Node()
            new.data=data
            new.address=check
            for i in range(Node.index-1):
                check=check.address
            check.address=new
        Node.index+=1
# *Constructor Method
    def __init__(self):
        self.data=None
        self.address=None
if __name__=='__main__':
    a=Node()
    a.append(2)
    a.append(3)
    a.append(4)
    print(a)
    print(a.search(4))
    print(a.search(9))