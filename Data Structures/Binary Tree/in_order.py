from samples import sample5, sample

def in_order(node):
    in_order(node.left) if node.left else None
    print(node.data, "$", end=' ')
    in_order(node.right) if node.right else None

if __name__ == '__main__':
    in_order(sample)
    print()
    in_order(sample5)