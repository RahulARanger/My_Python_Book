def bin_repr(number):
    while True:
        yield number % 2
        number //= 2
        
        if number == 0:
            break


# works as expected if the text has unique characters
def power_set(text):
    length = len(text)
    result = []
    
    expect = 2 << (length - 1)
    
    for _ in range(expect):
        index = 0 
        sub = ""
        
        for bit in bin_repr(_):
            
            if bit == 1:
                sub += text[index]
            
            index += 1
            
        result.append(sub)
        
    return result


print(power_set("abc"))
print(power_set("aa"))