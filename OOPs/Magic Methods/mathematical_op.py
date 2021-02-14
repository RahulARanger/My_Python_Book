class Num:
    def __new__(cls, number):
        if type(number) in [int, float]:
            return super().__new__(cls) # must call the super __new__ function
        else:
            raise TypeError("Given Number: {number} is not a Number")
    
        
    def __init__(self, number):
        self.value = number
        
    def __add__(self, other):
        return self.value + other
    
    def __sub__(self, other):
        return self.value - other
    
    def __mul__(self, other):
        return self.value * other
    
    def __truediv__(self, other):
        return self.value / other
    
    def __floordiv__(self, other):
        return self.value // other
    
    def __pow__(self, other):
        return self.value ** other


if __name__ == '__main__':
    a = Num(2)
    print(type(a))
    print(a + 3)
    print(a * 6)
    print(a / 1)
    print(a // 3)
    print(a ** 3)
    