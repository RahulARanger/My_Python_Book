from tkinter import*
class test(Tk):
    def __init__(self):
        super().__init__()
        self.test_frame=Frame(height=200,width=300,bg='orange')
        self.test_frame.config(cursor='heart')
        self.test_frame.pack()
test().mainloop()