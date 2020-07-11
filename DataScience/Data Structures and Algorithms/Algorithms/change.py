# this is the solution for the question 1 of the week 3 assignment 
n=int(input())
tens=n//10
n=n-tens*10
fives=n//5
n=n-fives*5
ones=n//1
print(ones+tens+fives)
