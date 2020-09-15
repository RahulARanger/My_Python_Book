from  string_exp_to_math_exp import *
from bracket import *
class I_P:
    def __init__(self,exp):
        self.exp=exp
        self.check()
        self.order=['/','*','+','-']
        
    def reverse_it(self):
        self.exp.reverse()
        for i in range(len(self.exp)):
            if self.exp[i]=='(':self.exp[i]=')'
            elif self.exp[i]==')':self.exp[i]='('

    def check(self):
        result,index=Checker(self.exp).test()
        if result is False:
            print('Please Check the Expression at:',index+1)
            assert False
        test=Tweak(self.exp)
        self.exp=test.convert()
        self.reverse_it()

    def convert(self):
        a=Stack()
        output=[]
        for i in self.exp:
            if type(i)==int or type(i)==float:
                output.append(i)
            elif i=='(':
                a.append(i)
            elif i==')':
                print(a)
                while a.getHead()!='(':
                    output.append(a.pop())
                a.pop()
            else:
                while True:
                    if a.len()==0:
                        a.append(i) 
                        break
                    elif a.getHead()=='(':
                        a.append(i)
                        break
                    else:
                        left=self.order.index(a.getHead())
                        right=self.order.index(i)
                        if left>right:
                            a.append(i) 
                            break
                        else:
                            output.append(a.getHead())
                            a.pop()
        while a.len()!=0:
            output.append(a.getHead())
            a.pop()
        return list(reversed(output))

if __name__=='__main__':
    a=I_P(input('Enter the Infix Expression: '))
    b=a.convert()
    print(b)

