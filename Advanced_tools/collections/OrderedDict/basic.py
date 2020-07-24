import collections
words=input('Enter some sentence: ').split()
a=collections.OrderedDict()
for i in words:
    a[i]=a.get(i,0)+1
print('The Frequency of the words in the sentence: ')
print(a)    