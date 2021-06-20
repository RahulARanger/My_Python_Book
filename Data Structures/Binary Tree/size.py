from samples import sample, sample5, sample2, sample6


def size(tree):
    return size(tree.left) + size(tree.right) + 1 if tree else 0

if __name__ == '__main__':
    print(size(sample))
    print(size(sample5))
    print(size(sample2))
    print(size(sample6))
