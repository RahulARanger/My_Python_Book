# find the median of the array if the two given sorted arrays were merged (preserving their sorted order)



def find(test1, test2):
    p1 = 0
    p2 = 0
    
    length1 = len(test1)
    
    length2 = len(test2)
    
    length = length1 + length2
    
    mode = length % 2 == 0
    target = (length // 2 - 1, length // 2 ) if mode else (length // 2, )
    done = 0
    sumed = 0
    print(target)
    
    for _ in range(length):
        if mode and done == 2:
            break
        
        if not mode and done == 1: 
            break
        
        if _ != target[done]:
            if test1[p1] < test2[p2]:
                p1 += 1
            else:
                p2 += 1
            continue 
        
        
        if p1 == length1:
            sumed += test2[p2]
            p2 += 1
        elif p2 == length2:
            sumed += test1[p1]
            p1 += 1
        else:
            if test1[p1] < test2[p2]:
                sumed += test1[p1]
                p1 += 1
            else:
                sumed += test2[p2]
                p2 += 1
        
        done += 1
        
        
    
    return sumed // 2 if mode else sumed
print(find([10, 20, 30], [5, 15, 25, 35, 45]))