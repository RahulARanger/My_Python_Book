# stock buy is a problem

# where we know sales of the product for the first n days (n > 1)
# and we have to find the maximum profit that we could gain from those prices

import array

# more precise ones

# def predict(test):
#     length = len(test)
    
#     low = 0 
#     buy = False
#     profit = 0
#     # print(test)
    
#     for day in range(1, length):
#         # print(day, profit, buy, low)
        
#         if day == length - 1:
#             if buy or test[low] > test[day]:
#                 break
            
#             profit += test[day] - test[low]
            
#         elif not buy and test[day] > test[day + 1] and test[low] < test[day]:
#             profit += test[day] - test[low]
#             buy = True
            
#         elif buy:
#             low = day
#             buy = False
            
#         else:
#             if test[low] > test[day]:
#                 low = day
#             else:
#                 pass
        
#     return profit


def predict(test):
    profit = 0
    
    for _ in range(1, len(test)):
        if test[_] > test[_ - 1]:
            profit += test[_] - test[_ - 1]
    
    return profit

sample1 = array.array('i', [1, 5, 3, 8, 12])
sample2 = array.array('i', [30, 20, 10])
sample3 = array.array('i', [10, 20, 30])
sample4 = array.array('i', [1, 5, 3, 1, 2, 8])

print(
    predict(sample1)
)

print(
    predict(sample2)
)

print(
    predict(sample3)
)

print(
    predict(sample4)
)
