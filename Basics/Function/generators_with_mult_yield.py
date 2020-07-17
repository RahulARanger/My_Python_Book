def oh():
    yield 'a'
    yield 'b'
    yield 'c'
g=oh()
print(next(g))
print(next(g))
print(next(g))
    