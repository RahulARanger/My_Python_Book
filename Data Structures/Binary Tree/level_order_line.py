from queue import Queue
from samples import sample, sample5, sample6, sample7


def level_order(tree):
    
    parser = Queue()
    parser.put(tree)
    
    while not parser.empty():
        
        for _ in range(parser.qsize()):
            obtained = parser.get()
            
            print(obtained.data, "$", end=' ')
            
            parser.put(obtained.left) if obtained.left else None
            parser.put(obtained.right) if obtained.right else None
        
        print()

def level_order_line_another(tree):
    if not tree:
        return

    parser = Queue()
    
    parser.put(
        tree
        )
    
    parser.put(
        None
        )
    
    while parser.qsize() > 1:
        obtained = parser.get()
        
        break_it = not obtained
        
        obtained = obtained if obtained else parser.get()
        
        print() if break_it else None
        
        print(
            obtained.data, "$", end=" "
            )
        
        parser.put(
            None
            ) if break_it else None
        
        parser.put(
            obtained.left
            ) if obtained.left else None
        
        parser.put(
            obtained.right
            ) if obtained.right else None

if __name__ == '__main__':
    level_order_line_another(sample)
    print('\n')
    level_order_line_another(sample5)
    print('\n')
    level_order_line_another(sample6)
    print('\n')
    level_order_line_another(sample7)
    print('\n')
    
    level_order(sample)
    print()
    level_order(sample5)
    print()
    level_order(sample6)
    print()
    level_order(sample7)
