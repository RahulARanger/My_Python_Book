def find_type(*a):
    print(type(a))# this is a tuple
    for i in a:
        print(i)
        print(type(i))
print('Enter any five elements of any data in that tht form : ')
a=eval(input())
b=eval(input())
c=eval(input())
d=eval(input())
e=eval(input())    
find_type(a,b,c,d,e)