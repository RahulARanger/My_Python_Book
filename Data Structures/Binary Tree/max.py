from samples import sample, sample5, sample7
import math

def max_node(tree):
    if not tree:
        return -math.inf
    
    return max(
        tree.data, max(
            max_node(tree.left), max_node(tree.right)
        )
    )

if __name__ == '__main__':
    print(max_node(sample))
    print(max_node(sample5))
    print(max_node(sample7))