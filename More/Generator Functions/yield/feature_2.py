# This tries to prove that yield dominates return

def check():
    n = 0

    while True:
        if n > 6:
            return 69
        else:
            yield n

        n += 1


collect = check()
print(type(collect))
for _ in range(8):
    try:
        print(next(collect))
    except StopIteration as error:
        print("Reached return statement, returned:", error)
