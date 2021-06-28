import array


def reverse(test):
    length = len(test)
    
    for _ in range(length // 2):
        test[_], test[length - _ - 1] = test[length - _ - 1], test[_]

def partial_reverse(test, start, end):
    while start < end:
        test[start], test[end] = test[end], test[start]
        start += 1
        end -= 1
    return test

sample = array.array('i', [int(_) for _ in input("Enter some Numbers: ").split()])

reverse(sample)
print(sample)

print(partial_reverse([1, 2, 3, 4, 5, 6, 7], 1, 2))
print(partial_reverse([1 ,2 ,3 ,4 ,5 , 6], 2, 5))

