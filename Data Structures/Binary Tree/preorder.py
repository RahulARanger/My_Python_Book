from samples import sample, sample5

def pre_order(tree):
    print(tree.data, "$", end=' ')
    pre_order(tree.left) if tree.left else None
    pre_order(tree.right) if tree.right else None

if __name__ == '__main__':
    pre_order(sample)
    print()
    pre_order(sample5)