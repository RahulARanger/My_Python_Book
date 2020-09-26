from tkinter import *
import tkinter.ttk as ttk
import string
class Main(Tk):
    def __init__(self):
        super().__init__()
        self.var1=StringVar()
        self.var1.set('Numbers')
        self.var2=StringVar()
        self.var2.set(1)
        self.var1.trace('w',self.change)
        self.nos=[i for i in string.digits]
        self.letters=[i for i in string.ascii_letters]
        self.a=OptionMenu(self,self.var1,'Letter','Numbers')
        self.b=ttk.Combobox(self,self.var2,*self.nos)
        self.menub=self.b['menu']
        self.a.config(width=6) #? Maintains the same width irrespective of the text
        self.a.pack(side=LEFT)
        self.b.pack(side=LEFT)
    def change(self,*args):
        self.menub.delete(0,END)
        what=self.var1.get()
        if what=='Letter':
            self.var2.set('a')
            for i in self.letters:
                self.menub.add_command(label=str(i))
        else: 
            self.var2.set('1')
            for i in self.nos:
                self.menub.add_command(label=str(i))

if __name__=='__main__':
    a=Main()
    a.mainloop()