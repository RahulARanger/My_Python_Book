import array


def reverse(test):
    length = len(test)
    
    for _ in range(length // 2):
        test[_], test[length - _ - 1] = test[length - _ - 1], test[_]

sample = array.array('i', [int(_) for _ in input("Enter some Numbers: ").split()])

reverse(sample)
print(sample)

