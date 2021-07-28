# given an unsorted array find two elements whose sum would yield as expected
# O(n) time, O(n) space 

def find_unsorted(test, key):
    container = {}
    
    for element in range(len(test)):
        container[element] = test[element]
    
    for element in test:
        if key - element in container:
            return container[element], container[key - element]
    
    return False

# given an sorted array find two elements whose sum would yield as expected
# O(n) time, O(1) space

def find_sorted(test, key, left=None, right=None):
    length = len(test)
    
    left = left if left else 0
    right = right if right else length - 1
    
    while left < right:
        check = test[left] + test[right]
        
        if check == key:
            return left, right

        if check > key:
            right -= 1
        
        else:
            left += 1
    
    return False

if __name__ == '__main__':
    print(find_sorted([2, 5, 8, 12, 30], 17))
    print(find_sorted([3, 8, 13, 18], 14))
        
        