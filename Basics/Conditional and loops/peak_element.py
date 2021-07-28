# a peak element in an array if that element is not smallest among its neighbors (left element and right element)


def find(test):
    length = len(test)
    left, right = 0, length - 1
    
    while left <= right:
        mid = left + right
        mid //= 2
        
        if (
            (mid == 0 or (test[mid] > test[mid - 1])) and (mid == length - 1 or (test[mid] > test[mid + 1]))
            ):
                return mid
        
        choice = mid + 1 
        
        choice = choice if mid == 0 else (mid - 1) if test[mid - 1] > test[mid] else choice
    
        if choice == mid + 1:
            left = choice
        else:
            right = choice
            
print(find([1, 2, 3]))
print(find([3, 2, 1]))
print(find([1, 10, 9, 3, 20, 4, 0]))
