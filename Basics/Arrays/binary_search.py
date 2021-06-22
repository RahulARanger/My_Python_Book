import array
import time

def bs(test: array.array, item: int):
    left, right = 0, len(test) - 1
    
    while left <= right:
        mid = (left + right) // 2
                
        if test[mid] == item or left == right:
            return test[mid] == item, mid
    
        left, right = (left, mid) if test[mid] > item else (mid + 1, right)
    
    return False, left
    

sample = array.array('i', range(565475469))

test = time.time()

print(bs(sample, 69))
print(bs(sample, 66))
print(bs(sample, 0))

test1 = time.time()

print(sample.index(69))
print(sample.index(66))
print(sample.index(0))

test2 = time.time()

print(test1 - test, test2 - test1)   # this proves the diff. of BS 

print(bs(sample, -2))
print(bs(sample, len(sample)))
