print(0 & 1)  # AND
print(0 | 1)  # OR

print()

print(~0)  # NOT
print(~1)  # we get negative value since compiler represents a number in 32 or 64 (depends on compiler)
print(~6)

print()

# bitwise operations, below will be applied for every bit representation of the number
print(4 | 3)  
print(6 & 9)

print()
# we know that 6 is 000...110 so,

# left - shift
print(6 >> 1)  # shifting all bits to right by 1  # 00...11
print(6 >> 2) # 000...1

print()
# right - shift
print(6 << 1)  # 000...1100
print(6 << 3)  # shifting all bits to left by 3  # 000...110000

# XOR (bitwise xor operation)

print(2 ^ 3)
print(3 ^ 3)