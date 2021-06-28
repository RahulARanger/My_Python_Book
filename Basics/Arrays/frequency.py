# frequency of the sorted array

def freq(test):
    pinned = test[0]
    
    collection = [
        [pinned, 1]
    ]
    
    for _ in range(1, len(test)):
        if pinned != test[_]:
            collection.append([test[_], 1]) 
            pinned = test[_]
        else:
            collection[-1][-1] += 1
    
    return collection

print(
    freq(sorted(range(10)))
)

print(
    freq([10, 10, 10, 25, 30, 30])
)

print(
    freq([10, 10, 10])
)

print(
    freq([10, 20, 30])
)

print(
    freq([10, 10, 10, 30, 30, 40])
)

print(
    freq([40, 50, 50, 50])
)

print(
    freq([1, 1, 1])
)