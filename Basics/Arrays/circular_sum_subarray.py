# circular subarrays includes all subarrays of an array and also
# the ones ones after connecting last index with the first index.
# think an array as an circular array (where last index and fist index are consecutive)

import array
import math


# we first find the max sum sub array and then for the pure circular sub arrays and then pick the max ones among them
# pure max sub array is nothing but the overall sum - min sum sub array
# sometimes overall and min sum subarray are of same length (hence 0) so we use warn
def scan(test):
	check = test[0]
	result = check
	overall = check
	
	for index in range(1, len(test)):
		overall += test[index]
		check = 0 if check < 0 else check
		check = check + test[index]
		
		result = max(result, check)

	check = test[0]
	temp_result = check
	
	for index in range(1, len(test)):
		check = 0 if check > 0 else check
		check = check + test[index]
		
		temp_result = min(temp_result, check)

	if check == 0:
		temp_result = -math.inf

	return max(result, overall - temp_result)

sample1 = array.array('i', [10, 5, -5])
sample2 = array.array('i', [5, -2, 3, 4])
sample3 = array.array('i', [2, 3, -4])
sample4 = array.array('i', [8, -4, 3, -5, 4])
sample5 = array.array('i', [-3, 4, 6, -2])
sample6 = array.array('i', [-8, 7, 6])
sample7 = array.array('i', [3, -4, 5, 6, -8, 7])
sample8 = array.array('i', [int(_) for _ in "7 -2 -2 -1 -24 29 28 20 -24 17 17 23 -11 24".split()])
sample9 = array.array('i', [int(_) for _ in "16 -1 28 24 1 -30 5 23 19".split()])
sample10 = array.array('i', [-18]) # reason for warn boolean variable

print(
	scan(sample1)
)

print(
	scan(sample2)
)

print(
	scan(sample3)
)

print(
	scan(sample4)
)

print(
	scan(sample5)
)

print(
	scan(sample6)
)

print(
	scan(sample7)
)

print(
	scan(sample8)
)

print(
	scan(sample9)
)

print(
	scan(sample10)
)