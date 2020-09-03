class Node:
    index=0
# TODO: Just a Printing method (Transversal Operation)
    def __str__(self):
        check=self
        collect=str()
        collect=str(check.data)+' '
        for i in range(Node.index-1):
            check=check.address
            collect+=str(check.data)+' '
        return collect 
# !deletion Operation
    def pop(self):
        if Node.index==0:
            print('List is Empty')
            return None
        elif Node.index==1:
            self.data=None
            self.address=None
        else:
            check=self
            for i in range(1,Node.index-1):
                check=check.address
            del check.address
            check.address=None
        Node.index-=1
# !deletion operation
    def popleft(self):
        if Node.index==0:
            print('The List is Empty')
            return None
        elif Node.index==1:
            self.data=None
            self.address=None
        else:
            check=self
            if check.address is not None:
                check.data=check.address.data
                check.address=check.address.address
        Node.index-=1    
# !insertion operation
    def append(self,data):
        if Node.index==0:
            self.data=data
        else:
            check=self
            while check.address is not None:
                check=check.address
            new=Node()
            new.data=data
            check.address=new
        Node.index+=1    
# !searching operation
    def search(self,value):
        check=self
        if check.data==value:return 0
        for i in range(1,Node.index):
            check=check.address
            if check.data==value:return i
        return -1    
# !insertion operation
    def appendleft(self,value):
        check=self
        new=Node()
        new.data=check.data
        new.address=check.address
        check.address=new
        check.data=value
# !insertion operation
    def insert(self,index,value):
        if index==1:
            self.appendleft(value)
        else:
            left=self
            for i in range(1,index):left=self.address
            print(left.data,left.address.data)
            right=Node()
            right.data=value
            right.address=left.address
            left.address=right
        Node.index+=1
# !deletion operation
    def delete(self,index):
        if index==Node.index:self.pop()
        elif index==1:self.popleft()
        else:
            check=self
            for i in range(1,index-1):
                check=check.address
            check.address=check.address.address
            Node.index-=13
# ! delete all elements
    def popall(self):
        check=self.address
        del check
        check=self
        check.data=None
        check.address=None
# ! setting the values
    def __setitem__(self,key,value):
        check=self
        for i in range(key):
            check=check.address
        check.data=value
# TODO: Sorting with the merge sort
    def __getitem__(self,key):
        check=self
        for i in range(key):
            check=check.address
        return check.data
    def getitem(self,key):
        check=self
        for i in range(key):
            check=check.address
        return check
    def sort_this(self):
        start=0
        end=Node.index
        self.sort(start,end)
    def sort(self,start,end):
        length=end-start+1
        print(start,end)
# TODO : Sorting with bubble sort
    def sort_b(self):
        check=self
        for i in range(Node.index):
            for j in range(Node.index):
                if i==j:continue
                if check[i]>check[j]:
                    print(check[i],check[j])
                    a=check[i]
                    check[i]=check[j]
                    check[j]=a
                    print(check[i],check[j])
        print(check)     
    def length(self):
        return Node.index
# TODO: A Constructor Function.
    def __init__(self,data=None):
        self.data=None
        self.address=None
        if type(data) is not None:
            pass
if __name__=='__main__':
    a=Node()
    n=int(input('Enter the Number of the Elements: '))
    for i in range(n):
        a.append(int(input('Enter the value: ')))
    print(a)    
    print(a[2])
    a.sort_b()
    print(a)