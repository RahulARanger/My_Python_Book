class Queue:
    index=0
    def __init__(self,data=None,size=1000):
        self.size=size
        if data is None:self.lst=[]
        elif type(data)==list:
            self.lst=data.copy()
            Queue.index=len(self.lst)
    def enqueue(self,data):
        if self.size==Queue.index:
            print('Queue is Full (Queue Overflow)')
            return None
        self.lst.append(data)
        Queue.index+=1
    def getFront(self):
        if Queue.index>0:return self.lst[0]
        else:
            print('Queue is Empty!!!')
            return None
    def __str__(self):
        combine=' '
        for i in self.lst:
            combine+=str(i)+' '
        return combine
    def deque(self):
        if Queue.index==0:
            print('Empty Queue!!! (Queue Underflow)')
            return None
        del self.lst[0]
        Queue.index-=1
if __name__=='__main__':
    a=Queue([1,2,3,4,5,6],size=20)
    a.enqueue(7)
    print(a)
    for i in range(3):
        a.deque()
    print(a)
    a.deque()
    print(a)
    for i in range(3):
        a.deque()