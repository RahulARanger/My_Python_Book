from Stack import *
import re
class Checker(Stack):
    def __init__(self,exp):
        self.exp=exp
        super().__init__(list(exp))
        self.check=list(reversed(self.toList()))
    def test(self):
        pairs={'}':'{',']':'[',')':'('}
        bracs=Stack()
        for i in range(len(self.check)):
            if self.check[i] in '{([':
                bracs.append(self.check[i])
            elif self.check[i] in '}])':
                if bracs.getHead()==pairs[self.check[i]]:
                    bracs.pop()
                else:return False,i
        if bracs.len()!=0:return False,bracs.len()-1
        return True,0

if __name__=='__main__':
    # ! This program only checks whether number of opening and closing brackets matches
    a=Checker(input('Enter the Expression to Check: '))
    result,index=a.test()
    if result:
        print('expression is Valid in terms of bracket arrangement and numberring (syntactically)')
    else:
        print('Please Check the Expression at:',index+1)