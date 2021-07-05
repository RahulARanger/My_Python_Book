def find(test):
    length = len(test)
    
    left, right = [0], [length - 1]
    
    for index in range(1, length):
        if test[left[-1]] > test[index]:
            left.append(index)
    
    for index in range(length - 2, -1, -1):
        if test[right[-1]] < test[index]:
            right.append(index)
            
    right.reverse()
    
    print("$", left)
    print(right)
    
    result = 0
    
    for righty in right:
        for lefty in left:
            if test[righty] >= test[lefty]:
                result = max(result, righty - lefty)
            
    return result
    
print(find([int(_) for _ in "82 63 44 74 82 99 82".split()]))
