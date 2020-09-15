class Queue:
    def __init__(self,cap=6):
        self.cap=cap
        self.lst=[0]*self.cap
        self.head,self.tail=-1,-1
    def append(self,data):
        if (self.head==0 and self.tail==self.cap-1) and (self.head-1==self.tail):
            print('Queue Overflow')
            assert  False
        if self.head==-1: self.head,self.tail=0,0
        if self.tail==self.cap:
            self.tail=0
        self.lst[self.tail]=data
        self.tail+=1
    def pop(self):
        if self.head==-1 or (self.head+1==self.tail):
            print('Queue Underflow')
            assert False
        else: 
            self.head+=1
    def __str__(self):
        start=self.head
        end=self.cap if self.tail<=self.head else self.tail
        round_2=True if self.tail<=self.head else False
        check=[]
        for i in range(start,end):
            check.append(self.lst[i])
        if round_2:
            for i in range(0,self.tail):
                check.append(self.lst[i])
        return str(check)
if __name__=='__main__':
    a=Queue()
    a.append(1)
    a.append(2)
    a.append(3)
    a.append(4)
    a.append(5)
    a.append(6)
    print(a)
    a.pop()
    print(a)
    a.append(7)
    print(a)
    a.pop()
    a.pop()
    a.pop()
    print(a)
    a.append(69)
    print(a)



