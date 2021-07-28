def find(test):
    steps = 0
    result = 0
    
    for index in range(1, len(test)):
        if test[index] > test[index - 1]:
            steps += 1
            result = max(steps, result)
        else:
            steps = 0 
    
    return result