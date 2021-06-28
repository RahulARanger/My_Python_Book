# left rotation is where we rotate the elements counter clock wise

# this is for left rotating an array by one place

import array


def left_rotate(test):
    safe = test[0]
    
    for _ in range(1, len(test)):
        test[_], test[_ - 1] = test[_ - 1], test[_]
    
    test[-1] = safe

contain = array.array('i', [int(_) for _ in input("Enter Numbers: ").split()])

left_rotate(contain)

print(
    contain
)
