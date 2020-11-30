# chr() converts the ascii value to the unicode string
a=(1,2)
print(ascii(a))
a=[1,2] 
print(ascii(a))
a={1:2}
print(ascii(a))
print(chr(97))
# ! ascii() is opposite of the eval() it returns the string format of any object
# * ord() converts the unicode to ascii value ( can take sting of length 1 not less or more than that)
print(ord('a'))