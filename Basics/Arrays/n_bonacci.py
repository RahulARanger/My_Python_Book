# fibonacci is 2 bonacci
# in n-bonacci series, first n - 1 elements are 0 and then 1
# given n and m return first m numbers of n bonacci series

def n_bonacci(n, m):
    result = [0 for _ in range(n - 1)]
    result.append(1)
    
    pinned = 0
    current = 1
    
    for _ in range(n, m):
        result.append(current)
        
        current += result[-1]
        current -= result[pinned]
        pinned += 1
    
    return result

print(n_bonacci(2, 10))
print(n_bonacci(5, 15))
