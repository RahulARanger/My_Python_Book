class Node:
    index=0
    def __init__(self,lst=None):
        self.data=None
        self.next=None
        self.prev=None
        if lst is not None:
            lst=list(lst)
            Node.index=0
            self.convert(lst)
    # TODO: Returns the index of the element 10  print(a.find(10))
    def find(self,value):
        for i in range(Node.index):
            if self[i]==value:return i
        return -1
    # TODO: coverts a list,set,string (any type that can be converted to list) is now Node() type
    def convert(self,lst):
        for i in lst:
            self.append(i)
    # TODO: appends the data of user type (so multiple types) can be entered/stored through this form
    def append(self,data):
        check=self
        if Node.index==0:
            check.data=data
        else:
            for i in range(Node.index-1):
                check=check.next
            new=Node()
            new.data=data
            new.prev=check
            check.next=new
        Node.index+=1
    # TODO: prints the doubly linked lists
    def __str__(self):
        collect=''
        check=self
        collect+=str(check.data)+' '
        for i in range(Node.index-1):
            check=check.next
            collect+=str(check.data)+' '
        return collect
    # ? Overloaded [] to know the nth element
    def __getitem__(self,key):
        check=self
        for i in range(key):
            check=check.next
        return check.data
    # ? to modify the nth value of the list
    def __setitem__(self,key,value):
        check=self
        for i in range(key):
            check=check.next
        check.data=value
if __name__=='__main__':
    a=Node()
    a=Node([int(i) for i in input('Enter the Numbers: ').split()])
    
# ! we can't actually slice right now unless we do some coding for that ( print(a[4:5]))
