# maximum difference between elements in array a[i2] - a[i1]
# such that i2 > i1

import array

def max_diff(test):
    mini = 0
    result = test[1] - test[0]
    
    for _ in range(1, len(test)):
        result = max(test[_] - test[mini], result)
        mini = mini if test[mini] < test[_] else _
    
    return result

sample1 = array.array('i', [2, 3, 10, 6, 4, 8, 1])
sample2 = array.array('i', [7, 9, 5, 6, 3, 2])
sample3 = array.array('i', [10, 20, 30])
sample4 = array.array('i', [30, 10, 8, 2])

print(
    max_diff(sample1)
)

print(
    max_diff(sample2)
)

print(
    max_diff(sample3)
)

print(
    max_diff(sample4)
)

sample = array.array('i', [int(_) for _ in input("Enter some Numbers: ").split()])

print(
    max_diff(sample)
)
