set_element = {1, 2, 3, 4, 5, 6}
set_element.remove(5)
set_element.discard(3)
try:
    set_element.remove(3)
except:
    print("There's an error in removing the element which is not there in the set")
print(set_element)
# we can avoid producing the error by deleting the element that isnt in set using discard() instead of remove()
# clear() deletes the every element in the set
# but the pop() removes the random element and then returns the removed element
while len(set_element) != 0:
    print(set_element.pop(), end=" ")
