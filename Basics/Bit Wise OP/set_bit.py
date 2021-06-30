# program to find whether kth bit from right is set (1) or not

# naive solution
# def check(number, pos):
#     for _ in range(pos - 1):
#         number /= 2
#     return number % 2 != 0

# O(1)
def check(number, pos):
    return (number >> pos - 1) % 2 == 1

print(
    check(
        5, 1
    )
)

print(
    check(
        8, 2
    )
)

print(
    check(
        13, 3
    )
)

print(
    check(
        0, 3
    )
)