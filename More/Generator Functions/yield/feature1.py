# by calling the generator function, we actually wont execute function

# unless we iterate over it

def check():
    n = 0

    while True:
        yield n
        n += 1


collect = check()
print(type(collect))  # return type is always an generator


print(next(collect))
print(next(collect))
