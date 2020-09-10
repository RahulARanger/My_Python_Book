
# TODO: using circular list we can rotate around the list any times
class Node:
    def __init__(self,lst=None):
        self.data=None
        self.next=None
        self.index=0
        if lst is not None:
            for i in lst:
                self.append(i)
    def append(self,data):
        if self.index==0:
            self.data=data
        else:
            check=self
            for i in range(self.index-1):
                check=check.next
            new=Node()
            new.data=data
            new.next=self
            check.next=new
        self.index+=1
    def insert(self,index,data):
        if self.index<index:
            assert(False,'List is EMPTY')
        elif self.index==index:
            self.append(data)
        elif index==0:
            new=Node()
            new.data=self.data
            new.next=self.next
            self.next=new
            new.data=data
            self.index+=1
        else:
            check=self
            for i in range(index):
                check=check.next
            new=Node()
            new.data=check.data
            new.next=check.next
            check.next=new
            check.data=data
            self.index+=1

    def pop(self):
        check=self
        if self.index==0:
            assert(False,'Empty List')
        elif self.index==1:
            self.data=None
        else:
            check=self
            for i in range(self.index-2):
                check=check.next
            check.next=self
        self.index-=1
    def __str__(self):
        lst=[]
        check=self
        for i in range(self.index-1):
            lst.append(check.data)
            check=check.next
        lst.append(check.data)
        return str(lst)
    def __getitem__(self,index):
        check=self
        for i in range(index):
            check=check.next
        return check.data
    def __setitem__(self,index,data):
        check=self
        for i in range(index):
            check=check.next
        check.data=data
if __name__=='__main__':
    a=Node([2,3,4,5])
    print(a)
    a.append(6)
    print(a)
    a.append(7)
    print(a)
    a.pop()
    print(a)
    a.insert(2,45)
    print(a)