check = (print(_) for _ in range(100))

# manually iterating
next(check)
next(check)
for _ in check:
    pass

try:
    next(check)
except StopIteration as error:
    print("all iterations of generator is exhausted!")
