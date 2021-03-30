from tkinter import *
import tkinter.ttk as ttk
import string
class Main(Tk):
    def __init__(self):
        super().__init__()
        self.var1=StringVar()
        self.var2=StringVar()
        self.var1.set('Default')
        self.ops=['Letters','Numbers']
        self.numbers=[i for i in string.digits]
        self.letters=[i for i in string.ascii_letters]
        self.a=ttk.Combobox(self,textvariable=self.var1,state='readonly',values=self.ops)
        self.var1.set('Numbers')
        self.var2.set('0')
        self.var1.trace('w',self.change)
        self.b=ttk.Combobox(self,textvariable=self.var2,state='readonly',values=self.numbers)
        self.a.pack(side=LEFT)
        self.b.pack(side=LEFT)
    def change(self,*ags):
        which=self.var1.get()
        if which=='Letters':
            self.b.config(values=self.letters)
            self.var2.set('a')
        else:
            self.b.config(values=self.numbers)
            self.var2.set('0')
            

if __name__=='__main__':
    Main().mainloop()