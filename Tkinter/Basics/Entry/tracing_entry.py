from tkinter import *
class App(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('600x600')
        self.text=StringVar()
        self.e=Entry(self,textvariable=self.text)
        self.text.trace('w',self.get)
        self.e.place(x=23,y=34)
    def get(self,*args):
        print(self.e.get())
a=App()
a.mainloop()
