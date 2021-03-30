
# * Refer this for even for more info : https://www.tutorialkart.com/python/tkinter/button/font/
from tkinter import *
from tkinter import font
class App(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('600x600')
        self.label=Label(self,text='Normal')
        self.custFont=font.Font(family='Comic Sans MS', size=22, weight='bold',underline=True,slant='italic')
        self.label2=Label(self,text='Bold',font=self.custFont)
        self.label2.place(x=23,y=50)
        self.label.place(x=23,y=34)
a=App()
a.mainloop()