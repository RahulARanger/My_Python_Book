# iterative form of the binary search
# searching for the index of key in sorted array

import array

def b_search(test, key):
    length = len(test)
    
    left = 0
    right = length - 1
    
    while right > left:
        mid = left + right
        mid //= 2
        
        if test[mid] == key:
            return True, mid
        
        if test[mid] > key:
            right = mid 
        else:
            left = mid + 1
    
    return test[right] == key, left

print(b_search(array.array('i', [10, 20, 30, 40, 50, 60]), 20))
print(b_search(array.array('i', [5, 15, 30]), 55))
print(b_search(array.array('i', [5, 10, 15, 25, 35]), 20))
print(b_search(array.array('i', [10, 15]), 20))
print(b_search(array.array('i', [10, 15]), 5))
print(b_search(array.array('i', [10, 10]), 10))
print(b_search(array.array('i', [1, 10, 10, 10, 20, 20, 40]), 20))
print(b_search(array.array('i', [10, 20, 30]), 15))
print(b_search(array.array('i', [15, 15, 15]), 15))
print(b_search(array.array('i', [15]), 15))