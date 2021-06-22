import array


# Refer: https://docs.python.org/3/library/array.html this for more info


note = array.array('i', [1, 2, 3])
print(note)
note.append(4)

try:
    note.append("check")
except TypeError:
    print("will be an error")

note.extend(range(100))

print(note.count(2))  # for counting the occurrence of the element 2
print(note.typecode)  # type of the array
print(note.itemsize)  # space occupied by each element

print(note.buffer_info())  # tuple of the address and the length of the array


# print(note.byteswap())  # swaps the array's elements into the bytes

note.reverse()
print(note)

note.reverse()

note.remove(99)
print(note.count(99))

print(note.pop())

print(note.pop(6))  # pops the 6th element from the last of the array


# we can't use nested array inside the built in array reason: check the type list in the website

