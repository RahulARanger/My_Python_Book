# maximum length of the subarray which has alternating odd and even numbers\
# uses kadens' algo: https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/

import array

def scan(test):
    toggle = test[0] % 2 == 0
    count = 1
    result = 1
    # print("%", test)
    
    for index in range(1, len(test)):
        if toggle == (test[index] % 2 == 0):
            count = 1
            continue
        
        count += 1
        result = max(count, result)
        toggle = not toggle
    
    return result


sample1 = array.array('i', [10, 12, 14, 7, 8])
sample2 = array.array('i', [7, 10, 13, 14])
sample3 = array.array('i', [10, 12, 8, 4])


print(
    scan(sample1)
)

print(
    scan(sample2)
)

print(
    scan(sample3)
)
