
# * Rem 
# ! Actually to append a element in the doubly linked list we need at least need to have length of the list=1
class Node:
    index=0
    back=None # * stores the location of the last object in the list
    def __init__(self):
        self.data=None
        self.prev=None
        self.next=None
# TODO: for printing in reverse or normal order
    def __str__(self,reverse=False):
        combine=''
        if not reverse:
            check=self
            combine+=str(check.data)+' '
            for i in range(Node.index-1):
                check=check.next
                combine+=str(check.data)+' '
        else:
            back=Node.back
            combine+=str(back.data)+ ' '
            for i in range(Node.index-1):
                back=back.prev
                combine+=str(back.data)+ ' '
        return combine
# TODO: to insert at the first position
    def appendleft(self,data):
        if Node.index==0:
            self.append(data)
        else:
            new=Node()
            check=self
            new.data=check.data
            new.prev=check
            new.next=check.next
            check.next.prev=new
            check.data=data
            check.next=new
            Node.index+=1
# TODO: to insert the node at the end of the list
    def append(self,data):
        if Node.index==0:
            Node.back=self
            self.data=data
        else:
            check=self
            for i in range(Node.index-1):
                check=check.next
            new=Node()
            new.data=data
            new.prev=check
            new.next=None
            check.next=new
            Node.back=new
        Node.index+=1
# TODO: to search for the element in the list
    def search(self,data):
        check=self
        if data==check.data:return 1
        for i in range(Node.index-1):
            check=check.next
            if check.data==data:return i+2
        return -1    
    def delete(self,index):pass
if __name__=='__main__':
    a=Node()
    for i in range(int(input('Enter the Number of elements: '))):
        a.append(int(input('Enter the value of the element: ')))
    print(a)
    print(a.__str__(reverse=True))
    result=a.search(int(input('Enter the value of the element to search for: ')))
    if result!=-1:
        print('The Element is found at {} '.format(result))
    else:
        print('Not found')