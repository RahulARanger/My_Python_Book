# iterative form of the binary search
# searching for the index of key in sorted array

import array

def last_found(test, key, left=-1, right=-1):
    length = len(test)
    left = left if left != -1  else 0
    right = right if right != -1 else length - 1
    
    while right > left:
        mid = left + right
        mid //= 2
        
        if test[mid] == key:
            
            if mid < length and test[mid] == test[mid + 1]:
                left = mid + 1
                continue
            
            return True, mid
        
        if test[mid] > key:
            right = mid 
        else:
            left = mid + 1
    
    return test[right] == key, left

if __name__ == '__main__':
    print(last_found(array.array('i', [10, 20, 30, 40, 50, 60]), 20))
    print(last_found(array.array('i', [5, 15, 30]), 55))
    print(last_found(array.array('i', [5, 10, 15, 25, 35]), 20))
    print(last_found(array.array('i', [10, 15]), 20))
    print(last_found(array.array('i', [10, 15]), 5))
    print(last_found(array.array('i', [10, 10]), 10))
    print(last_found(array.array('i', [1, 10, 10, 10, 20, 20, 40]), 20))
    print(last_found(array.array('i', [10, 20, 30]), 15))
    print(last_found(array.array('i', [15, 15, 15]), 15))
