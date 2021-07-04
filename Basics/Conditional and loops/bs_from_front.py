# given an array of unknown size find the element
import array

# Unbounded binary search


def actual(test, left, right, key):
    
    while left <= right:
        mid = left + right
        mid //= 2
        
        if test[mid] == key:
            return True, mid
        
        if test[mid] > key:
            right = mid - 1
        else:
            left = mid + 1
    
    return False, left
            
def b_search(test, key):
    if test[0] == key:
        return True, 0
    
    index = 1
    safe = 0
    
    while test[index] < key:
        safe = index
        index *= 2
        
    return actual(test, safe, index, key)

print(b_search(array.array('i', [10, 20, 30, 40, 50, 60]), 20))
print(b_search(array.array('i', [5, 10, 15, 25, 35]), 20))
print(b_search(array.array('i', [10, 15]), 5))
print(b_search(array.array('i', [10, 10]), 10))
print(b_search(array.array('i', [1, 10, 10, 10, 20, 20, 40]), 20))
print(b_search(array.array('i', [10, 20, 30]), 15))
print(b_search(array.array('i', [15, 15, 15]), 15))
print(b_search(array.array('i', [15]), 15))