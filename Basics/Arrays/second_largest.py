import array

def second_largest(test):
    main, second = None, None
    
    for _ in range(len(test)):
        main = main if main else test[_]
        
        main, second = (test[_], main) if test[_] > main else (main ,second)  
        # changing to >= will return same largest element if they have many max elements
    
    return second

sample = array.array('i', [int(_) for _ in input("Enter some Numbers: ").split()])

print(
    second_largest(sample)
)