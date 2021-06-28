import array

# returns the max numbers 1 arranged consectively

def scan(test):
    result = 0
    count = 0
    
    for _ in range(len(test)):
        if test[_] == 0:
            count = 0
        else:
            count += 1
            result = max(count, result)
    
    return result

sample1 = array.array('i', [0, 1, 1, 0, 1, 0])
sample2 = array.array('i', [1, 1, 1, 1])
sample3 = array.array('i', [0, 0, 0])
sample4 = array.array('i', [1, 0, 1, 1, 1, 1, 0, 1, 1])

print(
    scan(sample1)
)

print(
    scan(sample2)
)

print(
    scan(sample3)
)

print(
    scan(sample4)
)
