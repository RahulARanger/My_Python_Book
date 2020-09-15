class Stack:
    def __init__(self,lst=None):
        self.next=None
        self.data=None
        self.index=0
        if lst is not None:
            for i in lst:
                self.append(i)
    def append(self,data):
        if self.index==0:
            self.data=data
        else:
            new=Stack()
            new.data=self.data
            new.next=self.next
            self.next=new
            self.data=data
        self.index+=1
    def pop(self):
        if self.index==0:assert(False)
        else:
            self.data=self.next.data
            self.next=self.next.next
        self.index-=1
    def __str__(self):
        check=self
        print('|',end=' ')
        print(check.data,end=' ')
        print('|',end=' ')
        for i in range(self.index-1):
            check=check.next
            print(check.data,end=' ')
            print('|',end=' ')
        return ''
    def toList(self):
        lst=[]
        check=self
        for i in range(self.index-1):
            lst.append(check.data)
            check=check.next
        lst.append(check.data)
        return lst
if __name__=='__main__':
    a=Stack()
    a.append(2)
    a.append(3)
    a.append(4)
    a.append(5)
    a.append(6)
    a.append(7)
    print(a)
    a.pop()
    print(a)
    b=Stack([6,66,69,420])
    print(b)
    b.pop()
    b.pop()
    b.pop()
    print(b)