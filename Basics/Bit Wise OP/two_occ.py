# an array has all elements occuring even number of times
# there are 2 imposters find them

import array


# finds the kth bit of the number O(1)
def k_bit(number, k):
    return (number >> (k - 1)) % 2


# finds the index of the first set bit (O(log(n)))
def first_set(n):
    index = 1
    n = n if n % 2 == 0 else 1
    
    supporter = 2
    
    while n >= supporter:
        index += 1
        
        if n & supporter == supporter:
            return index
            
        supporter *= 2
        
        
    return index if n == 1 else 0

# finds the xor of the array of integers
def find_single(test):
    result = 0
    
    for _ in test:
        result ^= _
    
    return result


# finds the two imposters
def find(test):
    there, not_there = [], []
    
    index = first_set(
            find_single(test)
    )
    
    for _ in test:
        # print("->", _, k_bit(_, index), index)
        there.append(_) if k_bit(_, index) == 1 else not_there.append(_)
        
    # print("$", there, not_there, find_single(test), k_bit(find_single(test), first_set(find_single(test))), first_set(find_single(test)))
    return find_single(there), find_single(not_there)



print(find(array.array('i', [3, 4, 3, 4, 5, 4, 4, 6, 7, 7])))
print(find(array.array('i', [20, 15, 20, 16])))
print(find(array.array('i', [int(_) for _ in "4 2 4 5 2 3 3 1".split()])))
print(find(array.array('i', [int(_) for _ in "1 7 5 5 4 4".split()])))


# find the xor of the whole array, and then find the first set bit of that number
# then for sure there will be a imposter who has it and who doest have it
#  so we seprate it by checking the kth bit of every number in array
# by that we have there, not_there arrays
# now we can easily find the imposters in each arrays
