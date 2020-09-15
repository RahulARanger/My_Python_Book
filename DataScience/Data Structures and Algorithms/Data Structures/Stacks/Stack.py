
# ? Stack follows LIFO (last in first out) algo.
class Stack:
    def __init__(self,lst=None):
        self.index=0
        self.lst=[]
        if lst is not None:
            for i in lst:
                self.append(i)
    def append(self,data):
        # ! Normally when the number of elements exceeds the limit then it is stack overflow
        self.lst.insert(0,data)
    def len(self):
        return len(self.lst)
    def pop(self):
        try:
            store=self.lst[0]
            del self.lst[0]
            return store
        except:
            print('Stack UnderFlow')
            assert(False)
    def getHead(self):
        return self.lst[0]
    def __str__(self):
        print('|',end=' ')
        for i in self.lst:
            print(i,end=' ')
            print('|',end=' ')
        return ''
    def toList(self):
        return self.lst
if __name__=='__main__':
    a=Stack(['*','('])
    print(a)
    a.pop()
    print(a)
    