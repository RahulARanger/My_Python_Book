'''
problem statement:
A car starts from 'A' to 'B' and it can cover x distance with a full tank. There are n refill stations in the path
from 'A' to 'B' find the minimum number of refills required,if not possible print -1
'''
#link for visual representation for the problem : http://dm.compsciclub.ru/app/quiz-car-fueling
import sys
total_distance=int(input('Distance between starting and ending: '))
capacity=int(input('The capacity of the full tank: '))
lst=[int(i) for i in input('The positions of the stations: ').split()]
number_of_refils=0
start,end=0,capacity
if total_distance<=capacity:
    print(0)
    sys.exit(0)
travel_limit=capacity
start=0
tanks=[]
lst.append(total_distance)
for i in range(0,len(lst)-1):
    if lst[i]-start<=travel_limit:
        travel_limit-=(lst[i]-start)
        start=lst[i]
    else:
        print(-1)
        sys.exit(0)
    if lst[i+1]-lst[i]<=travel_limit:
        pass
    else:
        #print(travel_limit,lst[i+1],lst[i])
        number_of_refils+=1
        tanks.append(lst[i])
        travel_limit=capacity
if travel_limit>=total_distance:
    pass
else:
    print(-1)
    sys.exit(0)        
print(tanks)
print('The number of refeuls is {} '.format(number_of_refils)            )
