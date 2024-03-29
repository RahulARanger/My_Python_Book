# given the array is sorted

import array
import time

def filter_dup(test):
    index = 1
    
    for _ in range(1, len(test)):
        if test[_] != test[_ - 1]:
            test[index] = test[_]
            index += 1
        
    return index
    

sample = array.array('i', sorted([int(_) for _ in input("Enter some numbers: ").split()]))

print(
    sample[: filter_dup(sample)]
)

sample1 = sorted(list(range(10 ** 3)) + list(range(10 ** 3)))
sample2 = sorted(list(range(10 ** 6)) + list(range(10 ** 6)))

test1 = time.time()

filter_dup(sample1)
filter_dup(sample2)

test2 = time.time()

list(set(sample1))
list(set(sample2))

test3 = time.time()

print(
    test2 - test1, test3 - test2   # second method takes less time but more space
)
