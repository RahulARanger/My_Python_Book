class Deque:
    def __init__(self,lst=None):
        self.lst=[]
        if lst is not None:
            self.lst=lst
    def insertRear(self,data):
        self.lst.append(data)
    def insertFront(self,data):
        self.insert(0,data)
    def deleteFront(self):
        if len(self.lst)!=0:
            del self.lst[0]
        else:
            print('Queue Underflow')
    def deleteRear(self):
        if len(self.lst)!=0:
            del self.lst[len(self.lst)-1]
        else:
            print('Queue Underflow')
    def __str__(self):
        return str(self.lst)
if __name__=='__main__':
    a=Deque()
    a.insertRear(6)
    a.insertRear(9)
    print(a)
