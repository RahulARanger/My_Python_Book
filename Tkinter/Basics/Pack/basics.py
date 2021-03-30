from tkinter import *
class test(Tk):
    def __init__(self):
        super().__init__()
        self.bt=Button(self,bg='orange',text='Click me')
        self.bt.pack()
if __name__=='__main__':
    test().mainloop()