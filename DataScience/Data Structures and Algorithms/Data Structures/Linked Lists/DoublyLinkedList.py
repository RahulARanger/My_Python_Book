def merge(a,b):
    index_1,index_2=0,0
    ans=[]
    for i in range(len(a)+len(b)):
        if index_1>=len(a):
            ans.append(b[index_2])
            index_2+=1
        elif index_2>=len(b):
            ans.append(a[index_1])
            index_1+=1
        elif a[index_1]>b[index_2]:
            ans.append(b[index_2])
            index_2+=1
        else:
            ans.append(a[index_1])
            index_1+=1
    return ans
def mersort(a):
    if len(a)<3:
        if len(a)==2:
            if a[0]>a[1]:a[0],a[1]=a[1],a[0]
    else:
        mid=len(a)//2
        left=a[:mid]
        right=a[mid:]
        left=mersort(left)
        right=mersort(right)
        a=merge(left,right)
    return a
class Node:
    def __init__(self,lst=None):
        self.length=0
        self.data,self.prev,self.next=None,None,None
        self.tail=None
        if lst is not None:
            for i in lst:
                self.append(i)
    def append(self,data):
        if self.length==0:
            self.data=data
            self.tail=self
        else:
            check=self
            for i in range(self.length-1):
                check=check.next
            new=Node()
            new.data=data
            new.prev=check
            check.next=new
            self.tail=new
        self.length+=1
    def __str__(self):
        check=self
        lst=[check.data]
        for i in range(self.length-1):
            check=check.next
            lst.append(check.data)
        return str(lst)
    def getTail(self,for_='v'):
        if for_=='v':
            return self.tail.data
        else:
            return self.tail
    def getHead(self):
        return self.data
    def __getitem__(self,key):
        check=self
        for i in range(key):
            check=check.next
        return check.data
    def __setitem__(self,key,value):
        check=self
        for i in range(key):
            check=check.next
        check.data=value
    def delete(self,key):
        if key>self.length or self.length==0:
            assert (False,'Queue underflow')
        elif self.length==1:
            self.data=None
        elif key==self.length-1:
            check=self
            for i in range(self.length-2):
                check=check.next
            check.next=None
        else:
            check=self
            for i in range(key):
                check=check.next
            bye=check
            hi=check.next
            hi.prev=bye.prev
            bye.prev.data=bye.data
            bye.prev.next=bye.next
        self.length-=1
    def __delitem__(self,key):
        self.delete(key)
    def sort(self):
        # ? sorted using quick sort
        lst=[]
        check=self
        lst.append(check.data)
        for i in range(self.length-1):
            check=check.next
            lst.append(check.data)    
        lst=mersort(lst)
        return lst
    def find(self,key):
        for i in range(self.length):
            if self[i]==key:
                return i
        return -1
    def merge(self,a):
        if a.__class__.__name__=='Node':
            for i in range(a.length):
                self.append(a[i])
        else:
            for i in a:
                self.append(i)
if __name__=='__main__':
    a=Node([3,2,1,4])
    b=Node([5,9,10,7,6,10])
    print(a)
    print(b)
    # ? like the sorted()
    print(a.sort())
    a.merge(b)
    print(a)
    print(a.getTail())