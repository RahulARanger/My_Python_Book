import collections
lst=[int(i) for i in input().split()]
de=collections.deque(lst)
de.append(2)
de.appendleft(3)
de.append('e')
print(de)
while True:
    try:
        index=int(input('select any index position to delete: '))
        del de[index-1]
        break
    except:pass
print(de)  
de.remove('e')
# after removing the 