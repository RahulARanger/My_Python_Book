# an array is said to have a majority element
# if that element occurs more than half of the size of the array

import array

def majority(test: array.array):
    counted = 1
    length = len(test)
    selected = 0
    
    for _ in range(1, length):
        if test[_] == test[selected]:
            counted += 1
        
        else:
            counted -= 1
        
        if counted == 0:
            selected = _
            counted = 1
            
    return selected if test.count(test[selected]) > length // 2 else -1


sample1 = array.array('i', [8, 3, 4, 8, 8])
sample2 = array.array('i', [3, 7, 4, 7, 7, 5])
sample3 = array.array('i', [20, 30, 40, 50, 50, 50, 50])

print(
    majority(sample1)
)

print(
    majority(sample2)
)

print(
    majority(sample3)
)