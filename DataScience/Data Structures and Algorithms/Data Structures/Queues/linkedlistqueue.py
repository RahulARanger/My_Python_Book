class Queue:
    def __init__(self,lst=None):
        self.data=None
        self.next=None
        self.index=0
        if lst is not None:
            for i in lst:self.append(i)
    def append(self,data):
        if self.index==0:
            self.data=data
        else:
            check=self
            for i in range(self.index-1):
                check=check.next
            new=Queue()
            new.data=data
            check.next=new
        self.index+=1
    def pop(self):
        if self.index==0:
            print('Queue Underflow')
            assert False
        else:
            if self.index==1:self.data=None
            else:
                self.data=self.next.data
                self.next=self.next.next
            self.index-=1
    def __str__(self):
        lst,check=[],self
        for i in range(self.index-1):
            lst.append(check.data)
            check=check.next
        lst.append(check.data)
        return str(lst)
if __name__=='__main__':
    a=Queue()
    a.append(2)
    a.append(3)
    print(a)
    a.pop()
    print(a)
