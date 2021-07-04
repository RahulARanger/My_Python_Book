from first_found import first_found
from last_found import last_found

import array

def find(test, key):
    result, index = first_found(test, key)
    
    if not result:
        return False
    
    return last_found(test, key)[1] - index + 1


if __name__ == '__main__':
    print(find(array.array('i', [10, 20, 20, 20, 30, 30]), 20))
    print(find(array.array('i', [10, 10, 10, 10, 10]), 10))
    print(find(array.array('i', [5, 8, 10]), 7))
