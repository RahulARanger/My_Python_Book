# we can perform some mathematical operations on sets like
# union , difference,
a = {int(i) for i in input("Enter the numbers inside the set: ").split()}
b = {int(i) for i in input("Enter the numbers inside the set: ").split()}
print("The Union of the two sets is: {} ".format(a | b))
print("The Union of the two sets using union() is {} ".format(a.union(b)))
c = {int(i) for i in input("Enter the numbers inside the set: ").split()}
# print(a|b|c) is also possible
print(a.union(b, c))
print("The Intersection of a and b is {} ".fomat(a & b))
# same with a.intersection(b)
print("The Intersection of the three sets is {} ".foramt(a.intersection(b, c)))
# also possible with a&b&b
print("The set difference of the a and b is {}  ".format(a - b))
# can also be done with a.difference(b)
print("The symmertic differnce of the a and b is {} ".format(a ^ b))
