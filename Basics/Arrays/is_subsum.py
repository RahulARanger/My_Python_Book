# given an array return True if there's subarray of the given sum
# sliding window kind
# only for an array of non integer numbers

import array

# time complexity: O(2 * n) it's not quadratic
def check(test, amount):
    result = 0
    pin = 0
    
    for index in range(len(test)):
        result += test[index]
        
        if result == amount:
            return True
        
        while result > amount:
            result -= test[pin]
            pin += 1
    
    return result == amount

sample1 = array.array('i', [1, 4, 20, 3, 10, 5])

print(check(sample1, 23))
print(check(sample1, 15))
print(check(sample1, 3))
print(check(sample1, 12))

sample2 = array.array('i', [4, 7, -3, 1, 2])
print(check(sample2, 9))  # return False
# but there's 4, 7, -3, 1