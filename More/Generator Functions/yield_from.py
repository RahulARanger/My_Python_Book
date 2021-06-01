
# yield from iterable is the syntax for yielding element by element in a iterable

def check():
    yield from range(10)


for _ in check():
    print(_)
