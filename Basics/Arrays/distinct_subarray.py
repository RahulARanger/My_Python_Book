# count the number of the distinct elements in the subarray of size k
# haven't tested

def find(test, k):
    temp = {}
    result = []
    length = len(test)
    pin = 0
    
    for index in range(length):
        if (index + 1) % k == 0:
            result.append(len(temp))
            temp.pop(test[pin])
            pin += 1
        
        else:
            temp[index] = temp.get(index, 0) + 1
    
    return result
