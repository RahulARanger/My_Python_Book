from two_pointer import find_sorted

def find(test, key):
    length = len(test)
    
    for first in range(length):
        result = find_sorted(test, key - test[first], first + 1, length - 1)
        
        if not result:
            continue
        
        
        second, third = result
        
        if second != first and third != first:
            return first, second, third
    
    return False


print(find([2, 3, 4, 8, 9, 20, 40], 32))