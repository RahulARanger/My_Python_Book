
# TODO: In array implementation the node at the position 0 is root node
# TODO: odd indexes for the right node and even indices for the left node
class Heap:
    def __init__(self,lst=None):
        self.lst=[]
    def insert(self,element):
        self.lst.append(element)
        if len(self.lst)>1:self.manage()
        print(self)
    def manage(self):
        pos=len(self.lst)-1
        while True:
            current=pos
            if pos%2 == 0:pos=(pos)//2
            else:pos=(pos-1)//2
            if pos<0:break
            if self.lst[current]>self.lst[pos]:self.lst[pos],self.lst[current]=self.lst[current],self.lst[pos]
            if pos==0:break
    def delete_max(self):
        if len(self.lst)==1:
            self.lst.pop()
        else:
            self.lst[0],self.lst[-1]=self.lst[-1],self.lst[0]
            a=self.lst[-1]
            self.lst.pop()
            self.managepart2()
            return a
    def managepart2(self):
        pos=0     
        length=len(self.lst)   
        while True:            
            left=2*pos+1
            right=left+1
            print(self,left,right,pos)
            if left>=length:
                break
            else:
                special=False
                if right<length:
                    print(left,right,pos,'->',self.lst[pos],self.lst[left],self.lst[right])
                    if self.lst[pos]<self.lst[left] and self.lst[left]<self.lst[right]:
                        special=True
                if not special and self.lst[pos]<self.lst[left]:
                    self.lst[left],self.lst[pos]=self.lst[pos],self.lst[left]
                    pos=left
                    continue
            if right>=length:
                break
            else:
                if self.lst[pos]<=self.lst[right]:
                    self.lst[right],self.lst[pos]=self.lst[pos],self.lst[right]
                    pos=right
                    continue
                else:break
    def __str__(self):
        return str(self.lst)
if __name__=='__main__':
    a=Heap()
    a.insert(24)
    a.insert(7)
    a.insert(11)
    a.insert(5)
    a.insert(7)
    a.insert(6)
    a.insert(12)
    a.insert(10)
    a.insert(5)
    a.insert(10)
    check=[]
    for i in range(len(a.lst)):
        check.append(a.delete_max())
        print('*',a)
    print(a)
    print(check)
