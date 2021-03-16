'''
rotate() method is very useful method of the deque and it is not there in list

assume all the elements in deque arranged in the form of circle 
say lst=[1,1,2,6,6,4]
normal                  after rotate(2)                              after rotate(-2)
    1                        6                                              1
  4    1                  6     4                                        4     1
   6  2                     2   1                                         6  2
    6                          1                                           6
rotate(n): 
    clockwise if n is positive
    else anticlockwise
'''

import collections
lst=[int(i) for i in input().split()]
lst_right=lst.copy()
d1=collections.deque(lst)
d2=collections.deque(lst_right)
# we are now gonna rotate the elements of the deque which is not there in a list
d1.rotate(2)
d2.rotate(-2)
print('after right_rotation')
print(d1)
print('After left rotation')
print(d2)