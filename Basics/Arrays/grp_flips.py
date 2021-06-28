# given an array of binary numbers 
# we need to find min number of groups of bit (consecutive 1s or 0s) to make that array 
# filled with only one kind of digit (1 or 0)
# we can either flip 1 or 0 (that is use group of 1s or 0s)

import array


# this is the naive solution O(2 * n)
# def find(test):
#     _1 = 0 if test[0] == 0 else 1
#     _0 = 1 if test[0] == 0 else 0
    
#     length = len(test)
    
#     # print("%", test, is_0 , _0, _1)
    
#     for _ in range(1, length):
#         if test[_] != test[_ - 1]:
#             if test[_] == 1:
#                 _1 += 1
#             else:
#                 _0 += 1
    
#     if _0 == 0 or _1 == 0:
#         return ()
    
#     target = 0 if _0 < _1 else 1
    
#     target_ = []
#     over = True
    
#     for _ in range(length):
#         if test[_] == target:
#             if over:
#                 target_.append([_])
#                 over = False
#         else:
#             if not over:
#                 target_[-1].append(_ - 1)    
#                 over =  True
                
#     if not over:
#         target_[-1].append(length - 1)
    
#     return target_

# time complexity = O(1)

def find(test):
    is_1 = test[0] == test[-1] == 0 
    # if last and first element are same then that digit there's highest (0 or 1 here)'s group  or maybe there's only one digit
    # else then both are of same count
    target = []
    over = True
    length = len(test)
    
    for _ in range(length):
        if (test[_] == 1 and is_1) or (test[_] == 0 and not is_1):
            
            if not over:
                continue
            
            target.append([_])
            over = False
            
        else:
            if over:
                continue
            
            target[-1].append(_ - 1)
            over = True
    
    if not over:
        target[-1].append(length - 1)
    
    return target

sample1 = array.array('i', [1, 1, 0, 0, 0, 1])
sample2 = array.array('i', [1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1])
sample3 = array.array('i', [1, 1, 1])
sample4 = array.array('i', [0, 1])

print(
    find(sample1)
)

print(
    find(sample2)
)

print(
    find(sample3)
)

print(
    find(sample4)
)
