class Node:
    index=0
    def convert(self,n):
        for i in range(len(n)):
            self.append(int(n[i]))
    def __init__(self):
        self.data=None
        self.address=None
    def append(self,data):
        check=self
        if Node.index==0:
            check.data=data
        else:
            for i in range(Node.index-1):
                check=check.address
            new=Node()
            new.data=data
            check.address=new
        Node.index+=1
    def print(self):
        check=self
        print(check.data,end=' ')
        for i in range(Node.index-1):
            check=check.address
            print(check.data,end=' ')
    def appendleft(self,data):
        check=self
        new=Node()
        new.address=check.address
        new.data=check.data
        check.data=data
        check.address=new
        Node.index+=1
    def add_One(self):
        check=self
        for i in range(Node.index-1):
            check=check.address
        check.data+=1
        carry,pos=0,Node.index-1
        if check.data>=10:
            carry=check.data-9
            check.data-=10
        while carry!=0 and pos!=0:
            check=self
            for i in range(pos-1):
                check=check.address
            check.data+=1
            carry=0
            if check.data>=10:
                carry=check.data-9
                check.data-=10
                if pos==1:
                    self.appendleft(carry)
            pos-=1
if __name__=='__main__':
    a=Node()
    n=(input('Enter the Number: '))
    a.convert(n)
    a.print()
    print()
    a.add_One()
    a.print()