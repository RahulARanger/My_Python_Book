
#TODO: Heapify method is used to convet an array to the Heap

# TODO: insert method for inserting the elements at the correct place

# TODO: delete_max for deleting the max element and also maintains the Heap Structure

class Heap:
    def __init__(self,lst=None):
        self.lst=[]
        if lst is not None:
            self.heapify(lst)
    def heapify(self,lst): # ? max heap
        length=len(lst)
        nl=0
        if length%2==0:
            nl=length-(length//2)
        else:
            nl=length-((length+1)//2)
        self.lst=lst[:]
        for i in range(nl-1,-1,-1):
            self.check(i)            
    def check(self,a):
        pos=a
        length=len(self.lst)
        while True:            
            left=2*pos+1
            right=left+1
            if left>=length:break
            emergency=False
            at=left
            if right<length:
                if self.lst[left]<self.lst[right]:at=right
            else:emergency=True
            if self.lst[pos]<self.lst[at]:
                self.lst[pos],self.lst[at]=self.lst[at],self.lst[pos]
                pos=at
            else:emergency=True
            if emergency:break
    def __str__(self):return str(self.lst)
    def heapSort(self):
        ans=[]
        for i in range(len(self.lst)):
            ans.append(self.delete_max())
        return ans
    def insert(self,element):
        pos=len(self.lst)
        self.lst.append(element)
        while True:
            if pos%2==0:
                head=(pos-2)//2
            else:
                head=(pos-1)//2
            if head<0:break
            if self.lst[head]<self.lst[pos]:
                self.lst[head],self.lst[pos]=self.lst[pos],self.lst[head]
                pos=head
            else:break
    def delete_max(self):
        length=len(self.lst)
        if length==0:return
        else:
            self.lst[0],self.lst[-1]=self.lst[-1],self.lst[0]
            a=self.lst[-1]
            self.lst.pop()
            length-=1
            self.check(0)
            return a

if __name__=='__main__':
    b=[1,3,5,4,6,13,10,9,8,15,17]
    a=Heap(b)
    print(66*'*')
    print(a)
    print(66*'*')
    c=a.heapSort()
    c.reverse()
    print(c)
    print(66*'*')
    v=Heap()
    for i in b:
        v.insert(i)
    print(v)
    print(66*'*')
    f=v.heapSort()
    print(list(reversed(f)))
    print(66*'*')
    lst=[1,2,3,5,6,7,0]
    h=Heap(lst)
    print(h)