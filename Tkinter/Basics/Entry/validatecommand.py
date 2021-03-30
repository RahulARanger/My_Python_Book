from tkinter import *
from tkinter import font
root=Tk()
def check(text):
    print(len(text))
text=Entry(root,insertbackground='orange')
text.place(x=34,y=23)
root.mainloop()
