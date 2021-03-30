import re
import string
from tkinter import *
from tkinter import font
import pyglet
# TODO: This converts the given equation to the pure infix expressions
def convert_(eq):
    num=re.findall(r'([0-9.]+)',eq)
    sym=re.findall(r'([\(+\-*/\)])',eq)
    ans=[]
    flag=False
    symbols=['-','+','/','*','(',')']
    index_s=0
    index_n=0
    for i in eq:
        if i in symbols:
            ans.append(sym[index_s])
            index_s+=1
            flag=False
        elif i in string.digits and flag is False:
            flag=True
            ans.append(float(num[index_n]))
            index_n+=1
        elif flag is True:continue
        else:
            return None
    return ans

# TODO: reverses the characters and exhanges the brackets
def reverse_(eq):
    new=list(reversed(eq))
    for i in range(len(new)):
        if new[i]=='(':new[i]=')'
        elif new[i]==')':new[i]='('
        else:pass
    return new



# * Stack to support the conversion of the infix to the prefix expressions
class Stack:
    def __init__(self,eq):
        self.value=[]
        self.op=[]
        self.eq=eq
        
    def push(self,value):
        check=['/','*','+','-','(']
        if value=='(': self.value.append('(')
        else:
            while True:
                if len(self.value)==0:
                    self.value.append(value)
                    break
                elif check.index(self.value[-1])>check.index(value):
                    self.value.append(value)
                    break
                else:
                    self.op.append(self.value[-1])
                    self.value.pop()
    def pop_untill(self):
        while True:
            if self.value[-1]=='(':
                self.value.pop()
                break
            else:
                self.op.append(self.value[-1])
                self.value.pop()
    def normal_push(self,value):
        self.op.append(value)
    def to_List(self):
        return self.op
    def finale(self):
        while True:
            if len(self.value)==0:break
            self.op.append(self.value[-1])
            self.value.pop()
    def to_Prefix(self):
        for i in range(len(self.eq)):
            if self.eq[i]==')':
                self.pop_untill()
            elif type(self.eq[i])==float:
                self.normal_push(self.eq[i])
            else:
                self.push(self.eq[i])
        self.finale()
        self.final=list(reversed(self.to_List()))
        return self.final
    def evaluate(self):
        store=[]
        for i in range(len(self.final)-1,-1,-1):
            
            if type(self.final[i])==float:
                store.append(self.final[i])
            else:
                if self.final[i]=='+':
                    ans=store[-1]+store[-2]
                    for _ in range(2):store.pop()
                    store.append(ans)
                elif self.final[i]=='-':
                    ans=store[-1]-store[-2]
                    for _ in range(2):store.pop()
                    store.append(ans)
                elif self.final[i]=='*':
                    ans=store[-1]*store[-2]
                    for _ in range(2):store.pop()
                    store.append(ans)
                elif self.final[i]=='/':
                    ans=store[-1]/store[-2]
                    for _ in range(2):store.pop()
                    store.append(ans)
        return store[0]
class FrontEnd(Tk):
    def __init__(self):
        super().__init__()
        self.num=[]
        self.geometry('500x600')
        self.title('Calculator')
        self.output_font_=font.Font(family='KumbhSans',size=16,weight='bold')
        self.error=Label(self,font=self.output_font_,foreground='red',text='')
        self.resizable(0,0)
        self.arrangement()
    def do(self):
        try:
            Equation=Stack(reverse_(convert_(self.write.get())))
            Equation.to_Prefix()
            self.write.set('{:.3f}'.format(Equation.evaluate()))
        except:
            self.error.config(text='Wrong Expression')
    def clear_(self):
        self.write.set(' 0')
        self.error.config(text=' ')
    def back_(self):
        consider=self.op.index(INSERT)
        if consider==0:return None 
        check=list(self.write.get()) 
        left=check[:consider]
        right=check[consider:]
        left.pop()
        whole=''.join(left+right)
        self.write.set(whole)
        self.error.config(text=' ')
        self.op.icursor(consider-1)

    def display(self,bt):
        #if self.op.get()==' 0':self.write('')
        t=self.write.get()
        check=list(t)
        if t==' 0':
            self.write.set('')
            check=list(self.write.get())
        consider=self.op.index(INSERT)
        left=check[:consider]
        right=check[consider:]
        left.append(bt['text'])
        self.error.config(text=' ')
        text=''.join(left+right)
        print(consider)
        self.write.set(text)
        if consider==len(self.write.get()):
            pass
        else:
            self.op.icursor(consider+1)
    def arrangement(self):
        pyglet.font.add_file('Calculator\KumbhSans-Regular.ttf')
        self.write=StringVar()
        self.write.set(' 0')
        self.op=Entry(self,font=self.output_font_,justify='right',textvariable=self.write)
        for i in range(1,10):
            bt=Button(self,text=str(i))
            self.num.append(bt)
        self.zero=Button(self,text='0')
        self.lb=Button(self,text='(')
        self.rb=Button(self,text=')')
        self.plus=Button(self,text='+')
        self.mul=Button(self,text='*')
        self.div=Button(self,text='/')
        self.minus=Button(self,text='-')
        self.equal=Button(self,text='=')
        self.back=Button(self,text='<=')
        self.clear=Button(self,text='Clear')
        self.design()
    def design(self):
        for i in range(9):
            self.num[i].config(width=10,height=4,relief='groove',anchor='center')
        self.num[0].config(command=lambda:self.display(self.num[0]))
        self.num[1].config(command=lambda:self.display(self.num[1]))
        self.num[2].config(command=lambda:self.display(self.num[2]))
        self.num[3].config(command=lambda:self.display(self.num[3]))
        self.num[4].config(command=lambda:self.display(self.num[4]))
        self.num[5].config(command=lambda:self.display(self.num[5]))
        self.num[6].config(command=lambda:self.display(self.num[6]))
        self.num[7].config(command=lambda:self.display(self.num[7]))
        self.num[8].config(command=lambda:self.display(self.num[8]))
        self.op.config(relief='groove',width=32)
        self.zero.config(width=10,height=4,relief='groove',anchor='center',command=lambda:self.display(self.zero))
        self.rb.config(width=10,height=4,relief='groove',anchor='center',command=lambda:self.display(self.rb))
        self.lb.config(width=10,height=4,relief='groove',anchor='center',command=lambda:self.display(self.lb))
        self.plus.config(width=10,height=4,relief='groove',anchor='center',command=lambda:self.display(self.plus))
        self.mul.config(width=10,height=4,relief='groove',anchor='center',command=lambda:self.display(self.mul))
        self.div.config(width=10,height=4,relief='groove',anchor='center',command=lambda:self.display(self.div))
        self.minus.config(width=10,height=4,relief='groove',anchor='center',command=lambda:self.display(self.minus))
        self.equal.config(width=5,height=2,relief='groove',anchor='center',command=lambda:self.do())
        self.back.config(width=5,height=2,relief='groove',anchor='center',command=lambda:self.back_())
        self.clear.config(width=5,height=2,relief='groove',anchor='center',command=lambda:self.clear_())
        self.placements()
    def placements(self):
        self.op.place(x=60,y=75)
        self.num[0].place(x=60,y=120)
        self.num[1].place(x=160,y=120)
        self.num[2].place(x=260,y=120)
        self.plus.place(x=360,y=120)
        self.num[3].place(x=60,y=220)
        self.num[4].place(x=160,y=220)
        self.num[5].place(x=260,y=220)
        self.minus.place(x=360,y=220)
        self.num[6].place(x=60,y=320)
        self.num[7].place(x=160,y=320)
        self.num[8].place(x=260,y=320)
        self.mul.place(x=360,y=320)
        self.lb.place(x=60,y=420)
        self.rb.place(x=160,y=420)
        self.div.place(x=260,y=420)
        self.clear.place(x=60,y=15)
        self.back.place(x=400,y=15)
        self.zero.place(x=360,y=420)
        self.equal.place(x=200,y=15)

if __name__=='__main__':
    app=FrontEnd()
    app.mainloop()
