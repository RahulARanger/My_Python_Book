def add_any(*a):
    sum=0
    for i in a:
        for j in i:
            sum+=j
    return sum
a=input().split()
a=[int(i) for i in a]
a=add_any(a)
print('The sum of given numbers is: %d'%a)
#a=[int(i) for i in a]
#print(add_any(a))