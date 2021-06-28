# moving zero to end

import array

# nice
def move_zeros(test):
    pin = 0
    
    for _ in range(len(test)):
        if test[_] != 0:
            test[pin], test[_] = test[_], test[pin]
            pin += 1
    

sample = array.array('i', [int(_) for _ in input("Enter some Numbers: ").split()])

move_zeros(sample)

print(
    sample
)


sample1 = array.array('i', [0, 0, 0])
sample2 = array.array('i', [1, 0, 0, 0, 2, 3, 4])
sample3 = array.array('i', [8 ,5, 0, 10, 0, 20]) 

move_zeros(sample1)
move_zeros(sample2)
move_zeros(sample3)


print(
    sample1
    )

print(
    sample2
    )

print(
    sample3
    )