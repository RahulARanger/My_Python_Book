

# ! Here push(append) is easy task O(1) but for the pop it is of bit twisted task
# TODO: We can do this by two ways refer net (where push is bit twisted)
class Queue:
    def __init__(self,lst=None):
        self.lst=[]
    def append(self,data):
        self.lst.append(data)
    def len(self):
        return len(self.lst)
    def pop(self):
        if len(self.lst)==0:
            print('Queue Underflow')
            assert(False)
        check=self.lst[0]
        del self.lst[0]
        return check
class Stack:
    def __init__(self):
        self.a=Queue()
        self.b=Queue()
    def append(self,data):
        for i in range(self.a.len()):
            self.b.append(self.a.pop())
        self.a.append(data)
    def pop(self):
        self.a.pop()
        temp=Queue()
        for i in range(self.b.len()-1):
            temp.append(self.b.pop())
        self.a.append(self.b.pop())
        for i in range(temp.len()):
            self.b.append(temp.pop())
    def __str__(self):
        for i in self.b.lst:
            print(i,'|',end='')
        for i in self.a.lst:
            print(i,'|',end='')
        return ''
if __name__=='__main__':
    t=Stack()
    t.append(2)
    t.append(3)
    t.append(4)
    print(t)
    t.pop()
    print(t)
    t.append(5)
    print(t)
    t.pop()
    print(t)

