# vice versa to max sum subarray

import array

def scan(test):
    check = test[0]
    result = check
    
    for index in range(1, len(test)):
        check = 0 if check > 0 else check
        check = check + test[index]
        
        result = min(result, check)
    
    return result

sample1 = array.array('i', [2, 3, -8, 7, -1, 2, 3])
sample2 = array.array('i', [5, 8, 3])
sample3 = array.array('i', [-6, -1, -8])
sample4 = array.array('i', [3, -6, 1, 2, -1, 1, 2, -8, 1, 2, -4, 3])
sample5 = array.array('i', [-18])

print(
    scan(sample1)
)

print(
    scan(sample2)
)

print(
    scan(sample3)
)

print(
    scan(sample4)
)

print(
    scan(sample5)
)
