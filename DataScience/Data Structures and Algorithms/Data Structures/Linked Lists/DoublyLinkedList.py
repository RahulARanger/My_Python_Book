def quick_sort(lst,pivot=0,right=None):
    left_boundary=pivot
    right_boundary=right
    if right is None: right=len(lst)-1
    size=right-pivot+1
    if size<3:
        if size>1:
            if lst[pivot]>lst[right]:lst[right],lst[pivot]=lst[pivot],lst[right]
    else:
        left=pivot+1
        flag=0
        while right>=left:
            if flag==0:
                if lst[left]<=lst[pivot]:left+=1
                else:flag=1
            elif flag==1:
                if lst[right]>=lst[pivot]:right-=1
                else:flag=2
            elif flag==2:
                lst[left],lst[right]=lst[right],lst[left]
                flag=0
        lst[pivot],lst[right]=lst[right],lst[pivot]
        pivot,right=right,pivot
        quick_sort(lst,left_boundary,pivot-1)
        quick_sort(lst,pivot+1,right_boundary)

class Node:
    def __init__(self,lst=None):
        self.length=0
        self.data,self.prev,self.next=None,None,None
        if lst is not None:
            for i in lst:
                self.append(i)
    def append(self,data):
        if self.length==0:
            self.data=data
        else:
            check=self
            for i in range(self.length-1):
                check=check.next
            new=Node()
            new.data=data
            new.prev=check
            check.next=new
        self.length+=1
    def __str__(self):
        check=self
        lst=[check.data]
        for i in range(self.length-1):
            check=check.next
            lst.append(check.data)
        return str(lst)
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
        quick_sort(lst)
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
    a=Node()
    a.append(2)
    a.append(100)
    a.append(6)
    a.append(1)
    print(a)
    b=Node(a.sort())
    print(b)
    print(b.find(6))
    print(b.find(9))
    print(b.__class__.__name__)
    print(b,a)
    a.merge(b)
    print(b,a)
    a.merge([69,420])
    print(a)