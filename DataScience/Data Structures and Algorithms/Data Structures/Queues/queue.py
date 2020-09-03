class Entity:
    def __init__(self,lst=None):
        self.length=0
        self.lst=[]
        if lst is not None:
            for i in lst:
                self.enqueue(i)
    def enqueue(self,data):
        self.lst.append(data)
        self.length+=1
    def dequeue(self):
        if self.length>0:del self.lst[0]
        else:
            print('Queue Underflow')
    def getFront(self):
        return self.lst[-1]
    def getRear(self):
        return self.lst[0]
    def __str__(self):
        return str(self.lst)
if __name__=='__main__':
    a=Entity()
    a.enqueue(6)
    a.enqueue(9)
    a.enqueue(4)
    a.enqueue(2)
    a.enqueue(0)
    print(a)
    a.dequeue()
    a.dequeue()
    print(a)