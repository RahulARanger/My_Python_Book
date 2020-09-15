
# TODO: A queue requires two stacks for it's replacement on either linked list or arrays 

# ! here i have twisted the append( ) process there is another method where pop() is twisted refer net for that

class Stack:
    def __init__(self):
        self.lst=[]
    def append(self,data):
        self.lst.insert(0,data)
    def pop(self):
        if len(self.lst)==0:
            print('Stack Underflow')
            assert False
        check=self.lst[0]
        del self.lst[0]
        return check
    def len(self):
        return len(self.lst)
class Queue:
    def __init__(self):
        self.a=Stack()
        self.b=Stack()
    def append(self,data):
        self.a.append(data)
    def pop(self):
        for i in range(self.a.len()):
            self.b.append(self.a.pop())
        self.b.pop()
        for i in range(self.b.len()):
            self.a.append(self.b.pop())
    def __str__(self):
        for i in range(self.a.len()-1,-1,-1):
            print(self.a.lst[i],end=' ')
        return '' 
if __name__=='__main__':
    a=Queue()
    a.append(1)
    a.append(2)
    a.append(3)
    a.append(4)
    print(a)
    a.pop()
    print(a)
    a.pop()
    print(a)
    a.pop()
    a.pop()
    print(a)
    a.append(6)
    print(a)