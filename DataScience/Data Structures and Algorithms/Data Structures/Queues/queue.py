
# ? Queue Has two basic operations dequeue (removing elemeent from the front) and enqeue(adding element at the end)
# ? So Queue follows FIFO algo.
class Queue:
    def __init__(self,lst=None):
        self.lst=[]
        if lst is not None:
            self.lst=lst[:]
    def append(self,data):
        self.lst.append(data)
    def pop(self):
        try:
            del self.lst[0]
        except:
            print('Queue Underflow')
            assert False
    def __str__(self):
        return str(self.lst)
if __name__=='__main__':
    a=Queue()
    a.append(2)
    a.append(3)
    a.append(4)
    print(a)
    a.pop()
    print(a)