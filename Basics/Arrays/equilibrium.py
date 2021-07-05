# an array is said to have equilibrium point if the sum left to it is equal to the sum right to it

import array


def check(test):
    length = len(test)
    check_ = sum(test)
    until = 0

    for index in range(length):
        now = check_ - test[index] - until

        if now == until:
            return index

        until += test[index]

    return False


print(check(array.array('i', [3, 4, 8, -9, 20, 6])))
print(check(array.array('i', [4, 2, -2])))
print(check(array.array('i', [4, 2, 2])))
