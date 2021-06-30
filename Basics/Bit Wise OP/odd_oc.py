# in array every number occurs even number of times except the one
# find the imposter

import array

def find(test):
    result = 0
    
    for _ in test:
        result ^= _
    
    return result

print(find(array.array('i', [2, 2, 2, 3, 4, 3, 4])))
print(find(array.array('i', [69, 69, 69, 420, 420])))