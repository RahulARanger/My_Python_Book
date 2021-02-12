import math
import re
class Complex:
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary
    def __add__(self,others):
        orig_real=self.real+others.real
        orig_imaginary=self.imaginary+others.imaginary
        if orig_imaginary>=0:
            result='{:.2f}+{:.2f}i'.format(orig_real,orig_imaginary)
        else:
            result='{:.2f}{:.2f}i'.format(orig_real,orig_imaginary)    
        return result
    def __sub__(self,others):
        orig_real=self.real-others.real
        orig_imaginary=self.imaginary-others.imaginary
        if orig_imaginary>=0:
            result='{:.2f}+{:.2f}i'.format(orig_real,orig_imaginary)
        else:
            result='{:.2f}{:.2f}i'.format(orig_real,orig_imaginary)    
        return result
    def __mul__(self,others):
        orig_real=(self.real*others.real)-(others.imaginary*self.imaginary)
        orig_imaginary=(self.real*others.imaginary)+(others.real*self.imaginary)
        if orig_imaginary>=0:
            result='{:.2f}+{:.2f}i'.format(orig_real,orig_imaginary)
        else:
            result='{:.2f}{:.2f}i'.format(orig_real,orig_imaginary)    
        return result
    def __truediv__(self,others):
        answer=self*Complex.foil(others)
        result=re.findall(r'[0-9.]+',answer)
        if '-' not in answer[1:]:
            orig_imaginary=float(result[1])            
        else:
            orig_imaginary=float(result[1])*-1
        if answer[0]=='-':orig_real=float(result[0])*-1
        else:orig_real=float(result[0])
        mod_real=others.real**2+others.imaginary**2
        orig_real/=mod_real
        orig_imaginary/=mod_real
        if orig_imaginary>=0:
            result='{:.2f}+{:.2f}i'.format(orig_real,orig_imaginary)
        else:
            result='{:.2f}{:.2f}i'.format(orig_real,orig_imaginary)    
        return result    
    def mod(self):
        orig_real=self.real**2+self.imaginary**2
        orig_real=math.sqrt(orig_real)
        orig_imaginary=0
        result='{:.2f}+{:.2f}i'.format(orig_real,orig_imaginary)
        return result    
    @staticmethod
    def foil(number):
        number.imaginary*=-1
        lst=[number.real,number.imaginary]
        return Complex(*map(float,lst))
if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y,x-y,x*y,x/y,x.mod(),y.mod()]), sep='\n')