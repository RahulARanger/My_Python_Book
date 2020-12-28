def searchData(lst,key):
    flag=False
    for i in lst:
        if i==key:flag=True
    return True
print('Found:',searchData(range(1,100000000),3))