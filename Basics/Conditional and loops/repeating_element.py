# given an array of numbers in that one element repeats x number of times find that element
# given we have an array of 0 - at least n - 2

def find(test):
    limit = max(test)
    length = len(test)
    
    
    actual = (limit * (limit + 1)) // 2
    but = sum(test)
    
    repeating = length - limit
    
    found = 0
    
    for index in range(length):
        remove = test[index] * repeating
        
        if but - remove == actual:
            return test[index]
    
    return found


print(find([1, 3, 2, 4, 3, 3]))
print(find([1, 1]))
print(find([3, 4, 5, 1, 2, 1]))