# left rotating an array by n places

import array


def reversed_(test, start, end):
    while start < end:
        test[start], test[end] = test[end], test[start]
        start += 1
        end -= 1

def left_rotate(test, n):
    length = len(test)
    
    reversed_(test, 0, n - 1)
    reversed_(test, n, length - 1)
    reversed_(test, 0, length - 1)
    
    return test


def left_rotate_another(test, n):
    
    length = len(test)
    
    n = n % length if n >= length else n
    
    safe = test[: n]
    
    for _ in range(n, length):
        test[_], test[_ - n] = test[_ - n], test[_]
    
    
    test[-n: ] = safe

    return test


sample1 = array.array('i', [1, 2, 3, 4, 5]), 2
sample2 = array.array('i', [10, 5, 30, 15]), 3

print(
    left_rotate(*sample1)
)

print(
    left_rotate(*sample2)
)


print(
    left_rotate_another(*sample1)   # results wont be same because we are working on the changed ones
)

print(
    left_rotate_another(*sample2)
)
