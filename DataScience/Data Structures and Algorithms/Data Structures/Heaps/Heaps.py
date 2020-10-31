class Heap:
    def __init__(self,lst=None,Type=False):
        self.Type=Type # Max Heap if False else Min Heap
        if lst is None:self.lst=[]
        else:
            self.lst=lst[:]
            length=len(lst)
            if length%2==0:
                nl=length-(length//2)
            else:
                nl=length-((length+1)//2)
            for i in range(nl-1,-1,-1):
                self.heapify(i)
    def heapify(self,pos):
        # ? converts the array to the heap with a time complexity of O(n)
        while True:
            left=2*pos+1
            right=left+1
            if left<len(self.lst):
                at=left
            else:break
            if self.Type is False:
                if right>=len(self.lst):
                    if self.lst[at]>self.lst[pos]:
                        self.lst[pos],self.lst[at]=self.lst[at],self.lst[pos]
                    break
                else:
                    at=right if self.lst[right]>self.lst[left] else left
                if self.lst[at]>self.lst[pos]:
                    self.lst[pos],self.lst[at]=self.lst[at],self.lst[pos]
                    pos=at
                else:break
            else:
                if right>=len(self.lst):
                    if self.lst[at]<self.lst[pos]:
                        self.lst[pos],self.lst[at]=self.lst[at],self.lst[pos]
                    break
                else:
                    at=right if self.lst[right]<self.lst[left] else left
                if self.lst[at]<self.lst[pos]:
                    self.lst[pos],self.lst[at]=self.lst[at],self.lst[pos]
                    pos=at
                else:break
    def heapSort(self):
        #? Time Complexity O(nlogn)
        collect=[]
        for i in range(len(self.lst)):
            collect.append(self.lst[0])
            self.deleteHead()
        return list(reversed(collect)) if not self.Type else collect
    def insert(self,value):
        self.lst.append(value)
        pos=len(self.lst)-1
        while True:
            if pos%2==0:
                parent=(pos-2)//2
            else:
                parent=(pos-1)//2
            if parent<0:break
            if self.Type:
                if self.lst[parent]<self.lst[pos]:break
                else:
                    self.lst[parent],self.lst[pos]=self.lst[pos],self.lst[parent]
                    pos=parent
            else:
                if self.lst[parent]>self.lst[pos]:break
                else:
                    self.lst[parent],self.lst[pos]=self.lst[pos],self.lst[parent]
                    pos=parent
    def levelOrder(self):
        # ? O(n)
        return self.lst
    def maxi(self):
        # * Time Complexity is O(logn) for max heap but O(number of leaf nodes) for the min heap
        if self.Type is False:return self.lst[0]
        else:
            collect=[]
            for i in range(len(self.lst)-1,-1,-1):
                if 2*i+1>=len(self.lst):
                    collect.append(self.lst[i])
            return max(collect)
    def mini(self):
        # * Time Complexity is O(logn) for min heap but O(number of leaf nodes) for the max heap
        if self.Type is True:return self.lst[0]
        else:
            collect=[]
            for i in range(len(self.lst)-1,-1,-1):
                if 2*i+1>=len(self.lst):
                    collect.append(self.lst[i])
            return min(collect)
    def deleteHead(self,pos=0):
        length=len(self.lst)
        if length==1:
            self.lst.pop()
            return
        self.lst[pos],self.lst[-1]=self.lst[-1],self.lst[pos]
        self.lst.pop()
        length=len(self.lst)
        if self.Type is False:
            while True:
                left=2*pos+1
                right=left+1
                if left>=length:
                    break
                else:
                    check1=self.lst[left]
                if right>=length:
                    if check1>self.lst[pos]:
                        self.lst[pos],self.lst[left]=self.lst[left],self.lst[pos]
                    break
                else:
                    check2=self.lst[right]
                    selected=(check1,left) if check1>check2 else (check2,right)
                    if selected[0]>self.lst[pos]:
                        self.lst[pos],self.lst[selected[1]]=self.lst[selected[1]],self.lst[pos]
                        pos=selected[1]
                    else:break
        else: 
            while True:
                left=2*pos+1
                right=left+1
                if left>=length:
                    break
                else:
                    check1=self.lst[left]
                if right>=length:
                    if check1<self.lst[pos]:
                        self.lst[pos],self.lst[left]=self.lst[left],self.lst[pos]=self.lst[pos]
                    break
                else:
                    check2=self.lst[right]
                    selected=(check1,left) if check1<check2 else (check2,right)
                    if selected[0]<self.lst[pos]:
                        self.lst[pos],self.lst[selected[1]]=self.lst[selected[1]],self.lst[pos]
                        pos=selected[1]
                    else:break
    def findIt(self,value):
        # TODO: would be better if there are only unique elements in the Heap
        store= self.BSearch(0,len(self.lst)-1,value)
        return store
    def BSearch(self,start,end,value):
        if self.Type:
            mid=start+end+1
            mid//=2
            if start>end:return False
            if self.lst[mid]==value:return mid
            elif self.lst[mid]>value:return self.BSearch(start,mid-1,value)
            else:return self.BSearch(mid+1,end,value)
        else:
            mid=start+end+1
            mid//=2
            if start>end:return False
            if self.lst[mid]==value:return mid
            elif self.lst[mid]<value:return self.BSearch(start,mid-1,value)
            else:return self.BSearch(mid+1,end,value)
    def modify(self,from_,to):
        store=self.findIt(from_)
        if store is False:assert(False)
        self.deletePos(store)
        self.insert(to)
    def deletePos(self,pos):
        # TODO: would be better if there are only unique elements in the Heap
        length=len(self.lst)
        check=2*pos+1
        if check>length-1:
            del self.lst[pos]
            return
        self.deleteHead(pos)
if __name__=='__main__':
    lst=[1,2,3,5,6,7,0]
    a=Heap()
    [a.insert(i) for  i in lst]
    print(a.levelOrder())
    print(a.maxi())
    print(a.mini())
    b=Heap(Type=True)
    [b.insert(i) for i in lst]
    print(b.levelOrder())
    print(b.maxi())
    print(b.mini())
    b.deleteHead()
    print(b.levelOrder())
    c=Heap()
    [c.insert(i) for i in [20, 18, 10, 12, 8,  
            9, 3, 5, 6, 8]]
    print(c.levelOrder())
    print('Heap Sort: ',c.heapSort())
    c=Heap()
    [c.insert(i) for i in [20, 18, 10, 12, 8,  
            9, 3, 5, 6, 8]]
    print(c.mini())
    c.deleteHead()
    print(c.levelOrder())
    lst=[52,37,64,91,83,74,16,44,28,21]
    d=Heap()
    [d.insert(i) for  i in lst]
    print(d.levelOrder())
    print(d.findIt(64))
    d.deletePos(d.findIt(83))
    print(d.levelOrder())
    d.modify(44,100)
    print(d.levelOrder())
    lst=[52,37,64,91,83,74,16,44,28,21]
    e=Heap(lst,False)
    print(e.levelOrder())
    lst=[1,2,3,5,6,7,0]
    f=Heap(lst,True)
    print(f.levelOrder())