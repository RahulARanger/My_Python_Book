array = []

rows, cols = [int(_) for _ in input().split()]

for _ in range(rows):
    array.append([int(__) for __ in input().split()])

for _ in range(rows):
    for __ in range(cols):
        print(array[_][__], end=' ')
    print()

""" 
Test case:
3 3
1 2 3
4 5 6
7 8 9
"""