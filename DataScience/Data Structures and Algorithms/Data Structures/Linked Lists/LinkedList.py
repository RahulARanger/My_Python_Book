class Node:
    def __init__(self,lst=None):
        self.length=0
        self.address,self.data=None,None
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
    def delete(self,key=None):
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
    print(a,b)
    b.delete(2)
    print(b)