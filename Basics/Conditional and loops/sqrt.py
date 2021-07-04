# find the floor of sqrt of a number


# last value of the condition value ** 2 <= x
def sqrt(x):
    left = 1
    right = x
    ans = 1
    
    while left <= right:
        mid = left + right
        mid //= 2
        
        value = mid ** 2
        
        if value == x:
            return mid
        
        if value > x:
            right = mid - 1
        else:
            left = mid + 1
            ans = mid
    
    return ans


print(sqrt(10))
print(sqrt(4))
print(sqrt(14))
print(sqrt(25))