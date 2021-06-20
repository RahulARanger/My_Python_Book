from samples import sample, sample5

def post_order(tree):
    post_order(tree.left) if tree.left else None
    post_order(tree.right) if tree.right else None
    print(tree.data, "$", end=' ')

if __name__ == '__main__':
    post_order(sample)
    print()
    post_order(sample5)
    