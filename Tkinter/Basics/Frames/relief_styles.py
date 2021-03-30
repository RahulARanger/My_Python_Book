from tkinter import *
class test(Tk):
    def __init__(self):
        super().__init__()
        # ! Without borderwidth relief styles won't work for the frames so set borderwidth>0
        self.testing_frame=Frame(bg='orange',width=300,height=100)
        self.testing_frame.config(relief=SUNKEN)
        self.testing_frame.pack()
        self.testing=Frame(bg='blue',width=300,height=100,relief=GROOVE)
        self.testing.pack()
test().mainloop()