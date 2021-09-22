numbers = [1, 2, 3, 4, 5, 6, 7, 8, 66, 9]
big = small = None
for i in numbers:
    if small is None:
        small = i
    if big is None:
        big = i
    if small > i:
        small = i
    if big < i:
        big = i
print("the largest number in the list is:", big)
print("the smallest number in the list is:", small)
