class Node:
    def __init__(self,lst=None):
        self.next=None
        self.prev=None
        self.data=None
        self.index=0
        if lst is not None:
            for i in lst:
                self.append(i)
    def pop(self):
        if self.index==0:
            assert(False)
        else:
            temp=self.prev
            temp.prev.next=self
            self.prev=temp.prev
            self.index-=1
    def insert(self,index,data):
        if self.index==index:
            self.append(data)
        elif self.index<index:
            assert(False,'List Overflow')
        else:
            check=self
            for i in range(index):
                check=check.next
            new=Node()
            new.data=check.data
            new.next=check.next
            check.next.prev=new
            new.prev=check
            check.next=new
            check.data=data
            self.index+=1
    def append(self,data):
        if self.index==0:self.data=data
        else:
            check=self
            for i in range(self.index-1):
                check=check.next
            new=Node()
            new.data=data
            new.prev=check
            check.next=new
            new.next=self
            self.prev=new
        self.index+=1
    def __str__(self,times=1):
        lst=[]
        check=self
        go=self.index*times
        for i in range(go-1):
            lst.append(check.data)
            check=check.next
        lst.append(check.data)
        return str(lst)
if __name__=='__main__':
    a=Node([6,9,66])
    a.append(2)
    a.append(3)
    print(a)
    
    a.insert(0,1)
    print(a)
    a.insert(3,69)
    a.pop()
    print(a)
    print(a.__str__(times=3))
