from tkinter import *
calc=Tk()
calc['bg']='gold'
list_of_input=[]
def do_it(evalute_it,obj):
    lst_of_operations=[]
    print(evalute_it)
    lst_of_numbers=[]
    number=''
    for i in (evalute_it):
        if i.isnumeric() or i=='.':
            number+=i
        else:
            lst_of_numbers.append(float(number))
            number=''
            lst_of_operations.append(i)
    lst_of_numbers.append(float(number))
    number=''
    print(lst_of_numbers,lst_of_operations)            
    for operation in lst_of_operations:
        if operation=='+':
            answer=lst_of_numbers[0]+lst_of_numbers[1]
        elif operation=='-':
            answer=lst_of_numbers[0]-lst_of_numbers[1]                       
        elif operation=='*':
            answer=lst_of_numbers[0]*lst_of_numbers[1]    
        elif operation=='/':
            answer=lst_of_numbers[0]/lst_of_numbers[1]    
        del lst_of_numbers[0]
        lst_of_numbers[0]=answer
    obj.tweaks(str(lst_of_numbers[0]))

def collect_them(character):
    if character=='clear':
        for i in range(len(list_of_input)):
            list_of_input.pop()
    elif character=='back':
        list_of_input.pop()
    else:
        list_of_input.append(character)
    return ''.join(list_of_input)            
class window:
    answer='0'
    def __init__(self):
        self.output=Label(calc,text='Output:')
        self.output_display=Button(calc,text=self.answer,anchor='e',width=100,fg='black',bd=10,bg='orange',command=lambda: do_it(self.answer,self))
    def tweaks(self,character=answer):
        self.output.config(font=("Helvetica",12,'bold'),fg='orange',state=ACTIVE)
        self.output_display.config(font=("Helvetica",12,'bold'),relief=SUNKEN,text=character)        
        self.output.config(borderwidth=3,relief='solid',width=10)
        self.answer=character
    def start(self):
        self.tweaks()    
        self.output_display.place(x=15,y=45,width=550,height=66)
        self.output.place(x=15,y=15)
        calc.geometry('600x600')
        calc.title('Calculator')
        calc.mainloop()
class main(window):
    def __init__(self):
        super().__init__()
        self.plus=Button(calc,text='+',command=lambda :self.disable_them('+'))
        self.minus=Button(calc,text='-',command=lambda :self.disable_them('-'))
        self.divide=Button(calc,text='/',command=lambda :self.disable_them('/'))
        self.dot=Button(calc,text='.',command=lambda :self.enable_them('.'))
        self.change_sign=Button(calc,text='±',command=lambda :self.enable_them('c'))
        self.multiply=Button(calc,text='*',command=lambda :self.disable_them('*'))
        self.clear=Button(calc,text='clear',command=lambda :self.enable_them('clear'))
        self.back=Button(calc,text='←',command=lambda :self.enable_them('back'))
        self.zero=Button(calc,text='0',command=lambda :self.enable_them('0'))
        self.one=Button(calc,text='1',command=lambda :self.enable_them('1'))
        self.two=Button(calc,text='2',command=lambda :self.enable_them('2'))
        self.three=Button(calc,text='3',command=lambda :self.enable_them('3'))
        self.four=Button(calc,text='4',command=lambda :self.enable_them('4'))
        self.five=Button(calc,text='5',command=lambda :self.enable_them('5'))
        self.six=Button(calc,text='6',command=lambda :self.enable_them('6'))
        self.seven=Button(calc,text='7',command=lambda :self.enable_them('7'))
        self.eight=Button(calc,text='8',command=lambda :self.enable_them('8'))
        self.nine=Button(calc,text='9',command=lambda :self.enable_them('9'))
    def disable_them(self,character):
        wow=collect_them(character)
        self.divide.config(state=DISABLED,relief=RIDGE)
        self.minus.config(state=DISABLED,relief=RIDGE)
        self.multiply.config(state=DISABLED,relief=RIDGE)
        self.plus.config(state=DISABLED,relief=RIDGE)
        self.tweaks(wow)
        
    def tweaks1(self):
        self.zero.config(width=15,height=5,font=("Helvetica",10,'bold'),relief=SOLID,state=NORMAL)
        self.dot.config(width=15,height=5,font=("Helvetica",10,'bold'),relief=SOLID,state=NORMAL)
        self.change_sign.config(width=15,height=5,font=("Helvetica",10,'bold'),relief=SOLID,state=NORMAL)
        self.one.config(width=15,height=5,font=("Helvetica",10,'bold'),relief=SOLID,state=NORMAL)
        self.two.config(width=15,height=5,font=("Helvetica",10,'bold'),relief=SOLID,state=NORMAL)
        self.three.config(width=15,height=5,font=("Helvetica",10,'bold'),relief=SOLID,state=NORMAL)
        self.four.config(width=15,height=5,font=("Helvetica",10,'bold'),relief=SOLID,state=NORMAL)
        self.five.config(width=15,height=5,font=("Helvetica",10,'bold'),relief=SOLID,state=NORMAL)
        self.six.config(width=15,height=5,font=("Helvetica",10,'bold'),relief=SOLID,state=NORMAL)
        self.seven.config(width=15,height=5,font=("Helvetica",10,'bold'),relief=SOLID,state=NORMAL)
        self.eight.config(width=15,height=5,font=("Helvetica",10,'bold'),relief=SOLID,state=NORMAL)
        self.nine.config(width=15,height=5,font=("Helvetica",10,'bold'),relief=SOLID,state=NORMAL)
        self.plus.config(width=15,height=5,font=("Helvetica",10,'bold'),relief=SOLID,state=NORMAL)
        self.minus.config(width=15,height=5,font=("Helvetica",10,'bold'),relief=SOLID,state=NORMAL)
        self.divide.config(width=15,height=5,font=("Helvetica",10,'bold'),relief=SOLID,state=NORMAL)
        self.multiply.config(width=15,height=5,font=("Helvetica",10,'bold'),relief=SOLID,state=NORMAL)
        self.back.config(width=10,height=2,relief=SOLID)
        self.clear.config(width=10,height=2,relief=SOLID)    
    def enable_them(self,character):
        wow=collect_them(character)
        self.tweaks(wow)
        self.tweaks1()
    def place_them(self):
        self.tweaks1()
        self.one.place(x=15,y=156+12)
        self.two.place(x=146,y=156+12)
        self.three.place(x=277,y=156+12)
        self.four.place(x=15,y=256+6)
        self.five.place(x=146,y=256+6)
        self.six.place(x=277,y=256+6)
        self.seven.place(x=15,y=356)
        self.eight.place(x=146,y=356)
        self.nine.place(x=277,y=356)
        self.change_sign.place(x=15,y=450)
        self.zero.place(x=146,y=450)
        self.dot.place(x=277,y=450)  
        self.plus.place(x=430,y=168)
        self.minus.place(x=430,y=262)
        self.multiply.place(x=430,y=356)
        self.divide.place(x=430,y=450)
        self.back.place(x=480,y=120)
        self.clear.place(x=15,y=120)   
c=main()
c.place_them()
c.start()