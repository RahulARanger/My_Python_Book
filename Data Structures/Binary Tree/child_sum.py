from samples import sample3, sample2, sample11, sample12

def child_sum(tree):
    if not tree or not (tree.left or tree.right):
        return True
    
    left = tree.left.data if tree.left else 0
    right = tree.right.data if tree.right else 0

    return (left + right == tree.data) and child_sum(tree.left) and child_sum(tree.right)

if __name__ == '__main__':
    print(child_sum(sample3))
    print(child_sum(sample2))
    print(child_sum(sample11))
    print(child_sum(sample12))