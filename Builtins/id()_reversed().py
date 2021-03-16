
# TODO: id() returns the unique id() of the variable/Object which is valid until it's life time.
a=[1,2]
print(id(a))
b=a
# ! Aliasing
print(id(b),id(a))
# TODO: reversed() is another built in function which reverses the iterable object and then returns the object of the type reversed
a=input('Enter a String: ')
print('The reverse of the given string is: {}'.format(''.join(reversed(a))))
b=[1,2,3]
print('The Reverse of the list {} is : {} '.format(b,list(reversed(b))))
# !reversed() doesn't affect the original object hence it can used over strings too.