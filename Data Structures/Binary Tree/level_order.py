from queue import Queue
from samples import sample, sample5

def level_order(tree):
    if not tree:
        return

    parser = Queue()
    parser.put(tree)
    
    while not parser.empty():
        obtained = parser.get()
        print(obtained.data, "$", end=" ")
        
        parser.put(obtained.left) if obtained.left else None
        parser.put(obtained.right) if obtained.right else None
    

if __name__ == '__main__':
    level_order(sample)
    print()
    level_order(sample5)