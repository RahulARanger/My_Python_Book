import collections
lst=[int(i) for i in input().split()]
de=collections.deque(lst)
# appends from right (last index)
de.append(2)
# appends from the starting index 0
de.appendleft(3)
de.append('e')
print(de)
while True:
    try:
        index=int(input('select any index position to delete: '))
        # deleting by index
        del de[index-1]
        break
    except:pass
print(de)  
de.remove('e')
# after removing the element 'e' from the file