import array


def check(test):
    mode = -1
    pointer = test[0]
    
    for _ in range(1, len(test)):
        if test[_] == pointer:
            mode = mode
            
        elif test[_] > pointer:
            mode = 1 if mode == -1 else mode
            
            if mode != 1:
                return False # not ascending
        else:
            mode = 2 if mode == -1 else mode
            
            if mode != 2: 
                return False # not descending
        
        test[_] = pointer
    
    return mode

sample = array.array('i', [int(_) for _ in input("Enter some Numbers: ").split()])
print(
    check(sample)
)
