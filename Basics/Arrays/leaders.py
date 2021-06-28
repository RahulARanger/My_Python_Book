# leaders of the array 
# the elements to which there's no greater element to its right side

# example: 3 , 4, 6, 5 , 3, 1

# leaders: 3, 6, 5

import array

def leaders(test):
    pin = test[-1] 
    collect = [test[-1]]   # last one is always a leader
    
    for _ in range(len(test) - 1, -1, -1):
        collect.append(test[_]) if pin < test[_] else None
        pin = test[_] if pin < test[_] else pin
    
    return collect


test = array.array('i', [int(_) for _ in input("Enter the Numbers: ").split()])

print(
    leaders(test)
)


sample1 = array.array('i', [10, 20, 30])
sample2 = array.array('i', [30, 20, 10])
sample3 = array.array('i', [7, 10, 4, 10, 6, 5, 2])

print(
    leaders(sample1)
)

print(
    leaders(sample2)
)

print(
    leaders(sample3)
)
