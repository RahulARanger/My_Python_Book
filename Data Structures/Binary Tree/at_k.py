from samples import sample, sample4

def at_k(tree, k):
    if not tree:
        return None
    
    if k == 0:
        return print(tree.data, '$', end=' ')
    
    at_k(tree.left, k - 1) 
    at_k(tree.right, k - 1)

if __name__ == '__main__':
    at_k(sample, 2)
    print()
    at_k(sample4, 3)