n = int(input("Enter any Number: "))
lst = [_ for _ in range(1, n + 1) if _ % 2 == 0]
print("The list of first {} even numbers is : {}".format(n, lst))
lst = [
    _ for _ in range(0, n + 1) if _ % 2 == 0 if _ % 5 == 0
]  # its like and in if condition
print("The list of first {} multiples of 10 numbers is : {}".format(n, lst))
lst = [_ for _ in range(0, n + 1) if _ % 2 == 0 or _ % 5 == 0]
print("The list of first {} multiples of 2 and 5 numbers is : {}".format(n, lst))
