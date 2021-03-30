from tkinter import *
import tkinter.ttk as ttk
import string
# TODO: for more visit https://www.tcl.tk/man/tcl8.6/TkCmd/ttk_combobox.htm
class Main(Tk):
    def __init__(self):
        super().__init__()
        self.var1=StringVar()
        self.var2=StringVar()
        combostyle = ttk.Style()
        self.option_add("*TCombobox*Listbox*Background", "dodgerblue")
        self.option_add("*TCombobox*Listbox*selectBackground", "yellow")
        self.option_add("*TCombobox*Listbox*selectForeground", "pink")
        self.option_add("*TCombobox*Listbox*foreground", "orange")
        self.option_add("*TCombobox*Listbox*Font", "pirulen")
        combostyle.theme_create('combostyle', parent='clam',
                        settings = {'TCombobox':
                                    {'configure':
                                    {'selectbackground': '#007acc',
                                    'fieldbackground': '#007acc',
                                    'background': '#007acc',
                                    'foreground':'white',
                                    'arrowsize':15,
                                    'arrowcolor':'white',
                                    'bordersize':0,
                                    'padding':6,
                                    'lightcolor':'#007acc',
                                    'darkcolor':'#007acc',
                                    'font':('Helvtica',20,'bold'),
                                    'bordercolor':'#007acc',
                                    }}}
                        )
        combostyle.theme_use('combostyle') 
        self.var1.set('Default')
        self.ops=['Letters','Numbers']
        self.numbers=[i for i in string.digits]
        self.letters=[i for i in string.ascii_letters]
        self.a=ttk.Combobox(self,textvariable=self.var1,state='readonly',values=self.ops)
        self.var1.set('Numbers')
        self.var2.set('0')
        self.var1.trace('w',self.change)
        self.b=ttk.Combobox(self,textvariable=self.var2,state='readonly',values=self.numbers,style='rahul.TCombobox')
        
        self.a.pack(side=LEFT)
        self.b.pack(side=LEFT)
    def designs(self):
        pass
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