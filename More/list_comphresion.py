"""List comprehension exercises"""


def get_vowel_names(names):
    """Return a list containing all names given that start with a vowel."""
    return [name for name in names if name[0].lower() in "aeiou"]


def flatten(matrix):
    """Return a flattened version of the given 2-D matrix (list-of-lists)."""
    return [cell for row in matrix for cell in row]


def matrix_from_string(matrix):
    """Convert rows of numbers to list of lists."""
    return [[int(__) for __ in _.split(' ')] for _ in matrix.splitlines()]


def power_list(check):
    """Return a list that contains each number raised to the i-th power."""
    return [check[_] ** _ for _ in range(len(check))]


def matrix_add(matrix1, matrix2):
    """Add corresponding numbers in given 2-D matrices."""

    return [
        [
            matrix1[_][__] + matrix2[_][__]
            for __ in range(len(matrix1[0]))
        ]
        for _ in range(len(matrix1))
    ]


def identity(n):
    """Return an identity matrix of size x size."""
    return [[int(_ == __) for __ in range(n)] for _ in range(n)]


def triples(check):
    """Return list of Pythagorean triples less than input num."""
    return [
        (a, b, c)
        for a in range(1, check)
        for b in range(a + 1, check)
        for c in range(b + 1, check)
        if a ** 2 + b ** 2 == c ** 2
    ]
