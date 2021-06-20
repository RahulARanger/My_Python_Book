# sample tree (using references)

class Node:
    def __init__(self, data):
        self.data = data
        self.left, self.right = None, None
    

if __name__ == '__main__':
    a = Node(30)
    a.left = Node(40)
    a.right = Node(50)
    a.left.left = Node(70)
    a.right.right = Node(80)
