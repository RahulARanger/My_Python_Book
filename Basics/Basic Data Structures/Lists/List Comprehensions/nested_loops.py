matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)
transpose = []


def print_it(matrix):
    for i in range(len(matrix)):
        for j in matrix[i]:
            print(j, end=" ")
        print()


# this is normal way of transposing an matrix using the loops
print("The Original Matrix: ")
print_it(matrix)
for i in range(3):
    transpose.append([])
    for j in range(3):
        transpose[i].append(matrix[j][i])
print("Transpose of the Matrix using the loops: ")
print_it(transpose)
# Now we can transpose a matrix using the list comprehensions
transpose = [[matrix[j][i] for j in range(3)] for i in range(3)]
# they can even be other ways too (using the list comprehensions)
print("Transpose of the Matrix using the List Comprehensions: ")
print_it(transpose)
