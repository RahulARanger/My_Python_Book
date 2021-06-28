# given an array of integers and a number of k, find the max sum of k consecutive elements

# sliding window technique is widely used
import array

def find(test, k):
    check = sum(test[: k])
    result = check
    
    
    for index in range(k, len(test)):
        check -= test[index - k]
        check += test[index]
        
        result = max(check, result)
    
    return result

sample1 = array.array('i', [1, 8, 30, -5, 20, 7])
sample2 = array.array('i', [5, -10, 6, 90, 3])

print(
    find(sample1, 3)
)

print(
    find(sample2, 2)
)