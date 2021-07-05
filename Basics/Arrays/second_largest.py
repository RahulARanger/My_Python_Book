import array

def second_largest(test):
    main, second = test.index(max(test)), None
    
    for _ in range(len(test)):
        
        if _ == main:
            continue
            
        second = _ if second is None else second if test[second] > test[_] else _
    
    return second

sample = array.array('i', [int(_) for _ in input("Enter some Numbers: ").split()])

print(
    second_largest(sample)
)