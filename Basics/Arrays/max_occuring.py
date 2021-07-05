# we are given to find the maximum occuring elements from the left ranges and right ranges
# for example:
'''
n = 5
L[] = {1,5,9,13,21}
R[] = {15,8,12,20,30}

in this most occuring element is 5

what we do here is first create an array that contains all possible elements in the ranges

so we pick max element in the right range so here it is 30 so we have 32 (wait)

now we traverse from left to right in left and right ranges:
for left range:
we increment the value of that index by 1 

and for the right range we mark the stop by decrementing value of the index + 1  (so 32)


next we convert the temp array to the prefix array. this will have the count of the every element
and we add -1 to note the end of range

and then at last the find the index of the maximum element in that prefix array
'''


def find(left, right):
    maxi = max(right)
    
    temp = [0 for _ in range(maxi + 2)]
    
    for _ in left:
        temp[_] += 1
    
    for _ in right:
        temp[_ + 1] -= 1
    
    
    for _ in range(1, maxi + 1):
        temp[_] += temp[_ - 1]
    
    return temp.index(max(temp))