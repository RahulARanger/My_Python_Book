from Stack import *
from bracket import *
import string
import re
from string_exp_to_math_exp import *
class I_P:
    def __init__(self,exp):
        self.exp=exp
        self.order=['/','*','+','-']
        self.check_()
    def check_(self):
        result,index=Checker(self.exp).test()
        if not result:
            print('Please Check the Expression at:',index+1)
            assert(False)
        convert_=Tweak(self.exp)
        self.exp=convert_.convert()
        print(self.exp)
    def convert(self):
        a=Stack()
        output=[]
        for i in self.exp:
            if type(i)==int or type(i)==float:output.append(i)
            elif i=='(': a.append(i)
            elif i==')':
                while a.getHead()!='(': 
                    output.append(a.getHead())
                    a.pop()
                a.pop()
            else:
                while True:
                    if a.len()==0:
                        a.append(i)
                        break
                    elif a.getHead()=='(':
                        a.append(i)
                        break
                    left=self.order.index(a.getHead())
                    right=self.order.index(i)
                    if left>=right:
                        a.append(i)
                        break
                    else:
                        output.append(a.getHead())
                        a.pop()
        while a.len()!=0:
            output.append(a.getHead())
            a.pop()
        return output

if __name__=='__main__':
    a=I_P(input('Enter the Infix Experssion: '))
    b=a.convert()
    print('PostFix Expression:',b)
