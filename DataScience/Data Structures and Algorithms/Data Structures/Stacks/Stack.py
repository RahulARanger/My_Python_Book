class Plate:
    index=0
    def __init__(self,maxsize=100):
        self.lst=[]
        self.max=maxsize
    def push(self,data):
        if Plate.index==self.max:
            print('The Stack is Full!!! (Stack Overflow)')
        else:
            self.lst.append(data)
            Plate.index+=1
    def pop(self):
        if Plate.index==0:
            print('Stack is already Empty (Stack Underflow) ')
        else:
            self.lst.pop()
            Plate.index-=1
    def __str__(self,ch=' '):
        combine=''
        for i in self.lst:
            combine+=str(i)+ch
        return combine
    def isEmpty(self):
        return True if Plate.index==0 else False
    def isFull(self):
        return True if Plate.index==self.max else False
    def top(self):
        return self.lst[-1]
    def clear(self):
        Plate.index=0
        self.lst.clear()
    def topAndPop(self):
        if Plate.index==0:
            print('Stack is Already Empty (stack UnderFlow')
        else:
            r=self.lst[-1]
            self.lst.pop()
            return r
if __name__=='__main__':
    a=Plate(6)
    for i in range(1,7):
        a.push(i)
    print(a)
    a.push(7)
    for i in range(1,7):
        a.pop()
    print(a)
    a.pop()