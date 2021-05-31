import sys

check = (_ for _ in range(100))
check1 = [_ for _ in range(100)]


# for simple purposes, if we need to use list comprehension
# we can also save memory through generator expression
print(sys.getsizeof(check), sys.getsizeof(check1))
