from Infix_Prefix import *
from Stack import *
class Evalute(I_P):
    def __init__(self,exp):
        super().__init__(exp)
    def do_it(self):
        self.exp=self.convert()
        print(self.exp)
        output=[]
        a=Stack()
        for i in list(reversed(self.exp)):
            if type(i)==int or type(i)==float:
                a.append(i)
            else:
                A=a.pop()
                B=a.pop()
                do_lst={'+':A+B,'-':A-B,'*':A*B,'/':A/B}
                ans=do_lst[i]
                a.append(ans)
        return a.getHead()

if __name__=='__main__':
    a=Evalute(input('Enter the Infix Expression: '))
    b=a.do_it()
    print(b)
