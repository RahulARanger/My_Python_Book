from samples import sample, sample2, sample3, sample4

def height(tree):
    return max(
        height(tree.left) if tree.left else 0, height(tree.right) if tree.right else 0
        )  + 1 if tree else 0

if __name__ == '__main__':
    print(height(sample))
    print(height(sample2))
    print(height(sample3))
    print(height(sample4))