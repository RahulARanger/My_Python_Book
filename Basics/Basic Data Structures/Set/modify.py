set_elements = set({})
while True:
    num = input("Enter any Element to add: ")
    if num == "$":
        break
    set_elements.add(num)
set_elements.update([1, 2, 3, 4, 5, 6])
print(set_elements)
