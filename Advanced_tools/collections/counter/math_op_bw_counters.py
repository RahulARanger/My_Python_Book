import collections
print('Enter the List of elements: ',end='')
lst=[int(x) for x in input().split()]
print('\nEnter the list of elements: ',end='')
lst1=[int(x) for x in input().split()]
lst=collections.Counter(lst)
lst1=collections.Counter(lst1)
print()
# adds the values else creates ones (if note present from before)
print(lst + lst1)
# subs the values but removes the neg. values elements
print(lst - lst1)
# takes the elements of the min values of common elements alone
print(lst&lst1)
# takes their max values 
print(lst|lst1)
print(lst,lst1)