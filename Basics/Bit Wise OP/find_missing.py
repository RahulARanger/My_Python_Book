import array

def find(test):
    length = len(test)
    result = 0
    limit = max(test)
    
    for _ in range(limit + 1):
        if _ < length:
            result ^= test[_]
        
        result ^= _
    
    return result

print(find(array.array('i', [1, 4, 3])))
print(find(array.array('i', [1, 5, 3, 2])))
