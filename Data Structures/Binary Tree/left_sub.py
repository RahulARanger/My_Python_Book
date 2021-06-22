from samples import sample8, sample9, sample10
from queue import Queue

def left_view(tree):
    if not tree:
        return 
    
    level = -1
    
    def inner(node, level_):
        if not node:
            return 
        
        nonlocal level
        
        print(node.data, end=", ") if level_ > level else None
        level = level_ if level_ > level else level
        
        inner(node.left, level_ + 1) if node.left else None
        inner(node.right, level_ + 1) if node.right else None
    
    inner(tree, 0)
    

def left_view_level_order(tree):
    parser = Queue()
    parser.put(tree)
    
    while not parser.empty():
        for _ in range(parser.qsize()):
            test = parser.get()
            print(test.data, end=', ') if _ == 0 else None
            
            parser.put(test.left) if test.left else None
            parser.put(test.right) if test.right else None

if __name__=='__main__':
    left_view(sample8)
    print()
    left_view(sample9)
    print()
    left_view(sample10)
    print()
    left_view_level_order(sample8)
    print()
    left_view_level_order(sample9)
    print()
    left_view_level_order(sample10)
