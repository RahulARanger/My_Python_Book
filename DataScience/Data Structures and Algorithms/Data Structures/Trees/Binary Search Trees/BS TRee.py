
# TODO: to convert sorted array to the BS Tree it takes O(n) time complexity
# ! but to convert unsorted to BS Tree it takes O(logn) time complexity
class Node:
    def __init__(self,value,parent=None):
        self.value = value
        self.left=None
        self.parent=parent
        self.right=None
    def addRight(self,right):
        self.right=right
    def addLeft(self,left):
        self.left=left
class Tree:
    def __init__(self,lst):
        self.lst=lst
        self.head=None
        self.nlognway()
    def findNode(self,key):
        start=self.head
        if start.value==key:return self.head
        while True:
            if start is None:return False
            if key==start.value:
                return start
            elif key>start.value:
                start=start.right
            else:
                start=start.left
    def find(self,key):
        start=self.head
        while True:
            if start is None:return False
            if key==start.value:
                return True
            elif key>start.value:
                start=start.right
            else:
                start=start.left
    def nway(self):
        self.ans=[]
        self.head=self.sinsert(self.lst)
        return self.ans
    def nlognway(self):
        print(self.lst)
        for i in self.lst:
            self.insert(i) 
    def insert(self,data):
        if self.head is None:
            self.head=Node(data)
            return 
        start=self.head
        while True:
            if data>start.value:
                if start.right is None:
                    new=Node(data,start)
                    start.addRight(new)
                    return 
                else:
                    start=start.right
            elif data==start.value:
                assert False
            else:                
                if start.left is None:
                    new=Node(data,start)
                    start.addLeft(new)
                    return 
                else:start=start.left
    def inorder(self):
        self.ans=[]
        self.print_inorder(self.head)
        return self.ans
    def print_inorder(self,head):
        if head is  None:
            return 
        elif head.left is None:
            self.ans.append(head.value)
            self.print_inorder(head.right)
        else:
            self.print_inorder(head.left)
            self.ans.append(head.value)
            self.print_inorder(head.right)
    def levelOrder(self):
        # TODO: use queue for this
        start=self.head
        self.Q=[start]
        self.ans=[]
        self.print_levelorder()
        return self.ans
    def print_levelorder(self):
        while True:
            if len(self.Q)==0:return
            start=self.Q[0]
            left=start.left
            right=start.right
            if left is not None:
                self.Q.append(left)
            if right is not None:
                self.Q.append(right)
            self.ans.append(self.Q[0].value)
            del self.Q[0]
            if len(self.Q)==0:return
    def preOrder(self):
        self.ans=[]
        self.print_preorder(self.head)
        return self.ans
    def print_postorder(self,start):
        if start is None:return
        self.print_postorder(start.left)
        self.print_postorder(start.right)
        self.ans.append(start.value)
    def postOrder(self):
        self.ans=[]
        self.print_postorder(self.head)
        return self.ans
    def print_preorder(self,start):
        if start is None:return
        self.ans.append(start.value)
        self.print_preorder(start.left)
        self.print_preorder(start.right)
    def successor(self,value,object=False):
        p=self.findNode(value)
        right=p.right
        if right is None:
            # TODO: if the right is None then one of the node at the top(parents/grand parents) is the answer
            right=p
            while True:
                check=right.parent
                if check is None:
                    return
                if check.value>value:
                    return check if object else check.value
                else:
                    right=check
        while True:
            check=right.left
            if check is  None:
                if not object:
                    return right.value
                else:
                    return right
            right=check
    def predecessor(self,value,object=False):
        thisnode=self.findNode(value)
        if thisnode.left is None:
            check=thisnode.parent
            while True:
                if check is None:
                    return None
                else:
                    if check.value<value:
                        return check if object else check.value
                thisnode=check
        else:
            check=thisnode.left
            while True:
                if check.right is None:
                    return check.value if not object else check
                check=check.right
            
    def deleteIt(self,value):
        nodeto=self.findNode(value)
        if nodeto is False:assert(False)
        if nodeto.left is None and nodeto.right is None:
            if nodeto.parent is None:
                del self.head
                self.head=None
                return
            else:
                if nodeto.parent.left.value==nodeto.value:
                    nodeto.parent.left=None
                else:
                    nodeto.parent.right=None
            del nodeto
        elif nodeto.left is None or nodeto.right is None:
            carry=nodeto.left if nodeto.left is not None else nodeto.right
            if nodeto.parent is None:
                self.head=carry
                return
            if nodeto.parent.left.value==nodeto.value:
                nodeto.parent.left=carry
            else:
                nodeto.parent.right=carry
            del nodeto
        else:
            check1=self.predecessor(value,True)
            print(value)
            if check1 is not None:
                store=check1.value
                self.deleteIt(check1.value)
            else:
                check2=self.successor(value,True)
                store=check2.value
                self.deleteIt(check2)
            nodeto.value=store


    def mini(self):
        start=self.head
        while True:
            check=start.left
            if check is None:return start.value
            start=check
    def maxi(self):
        start=self.head
        while True:
            check=start.right
            if check is None:return start.value
            start=check

if __name__=='__main__':
    a=Tree([3,2,1])
    print(a.inorder())
    print('*'*66)
    a=Tree([99,35,19,0,11,40,5])
    print('Tree From:',[99,35,19,0,11,40,5])
    print('Level Order:',a.levelOrder())
    print('Inorder:',a.inorder())
    print('PreOrder:',a.preOrder())
    print('PostOrder:',a.postOrder())
    print('34 in Tree?',a.find(34))
    print('35 in Tree?',a.find(35))
    print('99 in Tree?',a.find(99))
    node=a.findNode(99)
    print(node.left.value)
    print('Succesor of 35 in tree:',a.successor(35))
    print('Succesor of 11 in tree:',a.successor(11))
    print('Minimum :',a.mini())
    a.deleteIt(99)
    print(a.levelOrder())
    print('*'*66)
    a=Tree([20,8,22,4,12,10,14])
    print('Tree from ',[20,8,22,4,12,10,14])
    print(a.successor(14))
    print(a.predecessor(14))
    print(a.predecessor(20))
    print(a.maxi())
    a.deleteIt(20)
    print(a.levelOrder())