# count the number of 1 in the binary repr of the number


# log(n)  n is length of the binary digits of the number

# def count(number):
#     counted = 0
    
#     if number % 2 != 0:
#         number -= 1
#         counted += 1
        
    
#     index = 2
#     while number >= index:
        
#         if number & index == index:
#             counted += 1
        
#         index <<= 1
    
#     return counted

# O(index)
def count(number):
    index = 0
    
    while number != 0:
        number &= number -1
        index += 1
    return index    

print(count(5))
print(count(7))
print(count(13))