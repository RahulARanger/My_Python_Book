import time

# if x is positive then left shift of x by is equal to x * 2 ^ y

x = 10 ** 10 

check = time.time()


answer = x << 69
time.sleep(1)

check2 = time.time()

answer2 = x * 2 ** 69
time.sleep(1)  # to get more precision

check3 = time.time()

print(check3 - check2, check2 - check)

# both are nearly same in terms of performance but it >> use single operator
print(answer == answer2)


# right shift of x by y is equal to x / ( 2 ** y)

answer = x >> 69
answer2 = x // (2 ** 69)

print(answer == answer2)