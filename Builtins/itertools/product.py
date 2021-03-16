import itertools
lst=[int(i) for i in input().split()]
lst1=[int(i) for i in input().split()]
lst2=[int(i) for i in input().split()]
print(list(itertools.product(lst,lst1,lst2)))

#another possibilites
print("The cartesian product using repeat:")  
print(list(itertools.product([1, 2], repeat = 2)))  
print()  
    
print("The cartesian product of the containers:")  
print(list(itertools.product(['geeks', 'for', 'geeks'], '2')))  
print()  
    
print("The cartesian product of the containers:")  
print(list(itertools.product('AB', [3, 4]))) 
