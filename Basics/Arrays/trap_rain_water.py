# Refer: https://www.geeksforgeeks.org/trapping-rain-water/

import array

# time complexity: O(n)
# space complexity: O(n)
def predict(test):
    right_block = test[-1]
    profit = 0
    
    length = len(test)
    rights = [length - 1]
    
    # first we mark the right blocks
    
    for block in range(length - 2, 0, -1):
        if test[block] >= right_block:
            rights.append(block)
            right_block = test[block]
            
    rights.reverse()  # we can also use index as length - 1 without reversing it
    # used for easy understanding
    
    index = 0
    # print(rights)
    
    left_block = 0
    
    # next we will loop directly and look at each block and subtract abs(right - left) - current
    for block in range(1, length):
        if rights[index] < block: 
            index += 1
        
        if test[block] > test[left_block]:
            left_block = block
            
        if test[block] <= test[rights[index]] and test[block] <= test[left_block]:
            profit += min(test[left_block], test[rights[index]]) - test[block]
            
    
    return profit
    
    

sample1 = array.array('i', [2, 0, 2])
sample2 = array.array('i', [3, 0, 1, 2, 5])
sample3 = array.array('i', [10, 20, 30])
sample4 = array.array('i', [30, 20, 10])
sample5 = array.array('i', [6, 1, 8, 9, 2, 7, 9, 5, 4, 3])
sample6 = array.array('i', [8, 8, 2, 4, 5, 5, 1])
sample7 = array.array('i', [1, 1, 5, 2, 7, 6, 1, 4, 2, 3]) # 7

print(
    predict(sample1)
)

print(
    predict(sample2)
)

print(
    predict(sample3)
)


print(
    predict(sample4)
)

print(
    predict(sample5)
)


print(
    predict(sample6)
)

print(
    predict(sample7)
)
