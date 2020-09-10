class Node:
    def __init__(self,lst=None):
        self.length=0
        self.address,self.data=None,None
    def insert(self,index,data):
        if self.length<index:
            assert(False,'List is EMPTY')
        elif self.length==index:
            self.append(data)
        elif index==0:
            new=Node()
            new.data=self.data
            new.next=self.next
            self.next=new
            new.data=data
            self.length+=1
        else:
            check=self
            for i in range(index):
                check=check.next
            new=Node()
            new.data=check.data
            new.next=check.next
            check.next=new
            check.data=data
            self.length+=1
    def append(self,data):
        if self.length==0:
            self.data=data
        else:
            check=self
            for i in range(self.length-1):
                check=check.address
            new=Node()
            new.data=data
            check.address=new
        self.length+=1
    def __str__(self):
        lst=[self.data]
        check=self
        for i in range(self.length-1):
            check=check.address
            lst.append(check.data)
        return str(lst)
    def __getitem__(self, key):
        check=self
        for i in range(self.length-1):
            check=check.address
        ans=check.data
        return ans
    def __setitem__(self,key,value):
        check=self
        for i in range(key):
            check=check.address
        check.data=value
    def __delitem__(self,key):
        if key is None: key=self.length-1
        if key>self.length or self.length==0:
            print('Not enough size')
            return None
        elif self.length==1:
            self.data=None
        elif key==self.length-1:
            check=self
            for i in range(self.length-2):
                check=check.address
            check.address=None
        else:
            check=self
            for i in range(key):
                check=check.address
            bye=check
            check=self
            for i in range(key+1):
                check=check.address
            hi=check
            bye.data=hi.data
            bye.address=hi.address
        self.length-=1
if __name__=='__main__':
    a=Node()
    a.append(6)
    a.append(9)
    print(a)
    b=Node()
    b.append(6)
    b.append(8)
    b.append(3)
    print(b.length)
    b.insert(2,45)
    print(a,b)
    del b[2]
    print(b)