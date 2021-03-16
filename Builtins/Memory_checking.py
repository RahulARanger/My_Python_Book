import sys

a = int(input('Enter the Value of the variable (integer): '))
print('{} bits'.format(sys.getsizeof(a)))
b = input('Enter some text: ')
print('{} bits'.format(sys.getsizeof(b)))
