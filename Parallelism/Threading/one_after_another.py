from tkinter import *
class test(Tk):
    def __init__(self,text_):
        super().__init__()
        self.bt=Button(self,text=text_,command=self.boom)
        self.bt.pack()
    def boom(self):
        self.destroy()
a=test('Window 1')
a.mainloop()
b=test('Window 2')
b.mainloop()