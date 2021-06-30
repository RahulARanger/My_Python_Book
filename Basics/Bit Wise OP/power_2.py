# check if the given number is power of 2
# a number which is power of 2 has only 1 set bit except number 1 

def check(number):
    return False if number == 0 else (number & number - 1) == 0

print(check(2))
print(check(69))
print(check(48))
print(check(32))
