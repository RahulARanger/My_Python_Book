from tkinter import*
class test(Tk):
    def __init__(self):
        super().__init__()
        self.test_frame=Frame(height=200,width=300,bg='orange')
        self.test_frame_2=Frame(height=200,width=300,bg='skyblue')
        self.test_frame.pack(side=LEFT)
        self.test_frame_2.pack(side=LEFT)
        # LEFT, RIGHT, TOP are the available values
test().mainloop()