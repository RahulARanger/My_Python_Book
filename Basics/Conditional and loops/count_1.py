# given an array of binary numbers and they are sorted, find the count for the number 1

from first_found import first_found
from last_found import last_found
import array

def count(test):
    result, index = first_found(test, 1)
    
    if not result:
        return False
    
    last = last_found(test, 1)[-1] if index == 0 else len(test) - 1
    
    return last - index + 1


print(count(array.array('i', [0, 0, 1, 1, 1, 1])))
print(count(array.array('i', [1, 1, 1, 1, 1, 1])))
print(count(array.array('i', [0, 0, 0, 0])))