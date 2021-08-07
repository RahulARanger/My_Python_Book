from linked_list import SingleNode

def last_th(test: SingleNode, k):
    store = None
    
    for _ in range(k):
        test = test.next if test else None
    
    store = test
    
    while test:
    
        for _ in range(k + 1):
            test = test.next if test else None
            
        store = test if test else store
    
    return store

Sample1 = SingleNode()

[Sample1.append(SingleNode(_ * 6)) for _ in range(6)]


Sample1 = SingleNode()

[Sample1.append(SingleNode(_ * 6)) for _ in range(6)]

print(last_th(Sample1, 0).value)
print(last_th(Sample1, 2).value)
