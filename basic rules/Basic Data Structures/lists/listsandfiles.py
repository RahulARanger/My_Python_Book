#display the words in the file in dictionary order and display them so that there are no duplicate words
fname=input('Enter the Name of the File: ')
hand=open(fname)
lists=[]
for i in hand:
    listed=i.split()
    lists=lists+listed
sets=set(lists)
lists=list(sets)
lists.sort()
print(lists)