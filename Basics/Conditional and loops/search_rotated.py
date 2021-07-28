# search in sorted and rotated array refer: https://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/

def check(test, key):
    left = 0
    right = len(test) - 1
    
    while left <= right:
        print("$", left, right)
        mid = left + right
        mid //= 2
        
        if test[mid] == key:
            return True, mid
    
        if test[mid] > test[left]: # left ones is supported
            if (key >= test[left] and key <= test[mid - 1]):  
                right = mid - 1
            else:
                left = mid + 1
        else:  # right ones is sorted
            if (key >= test[mid + 1] and key <= test[right]):
                left = mid + 1 
            else:
                right = mid - 1

    return False, left, right


print(check([10, 20, 40, 60, 5, 8], 5))
print(check([10, 20, 40, 60, 5, 8], 60))
print(check([10, 20, 40, 60, 5, 8], 63))
print(check([5, 6, 1, 2, 3, 4], 1))