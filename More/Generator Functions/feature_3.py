def check():
    n = 0
    print("start")

    while n <= 6:
        yield n
        print("looping")
        n += 1

    print("end")


# another proof that generator starts executing while iterating over it

sample = check()  # generator object
print("see no output")

for _ in check():
    print(_)
