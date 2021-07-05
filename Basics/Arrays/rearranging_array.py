# aims to rearrange the array with the space complexity of O(1)
# refer: https://practice.geeksforgeeks.org/problems/-rearrange-array-alternately-1587115620/1/?track=DSASP-Arrays&batchId=154

def rearrange(test):
    length = len(test)
    max_value = test[-1] + 1
    
    refer = length - 1 
    
    for index in range(0, length, 2):
        test[index] += (test[refer] % max_value) * max_value
        refer -= 1
    
    refer = 0
    for index in range(1, length, 2):
        test[index] += (test[refer] % max_value) * max_value
        refer += 1
    
    for index in range(0, length):
        test[index] //= max_value
