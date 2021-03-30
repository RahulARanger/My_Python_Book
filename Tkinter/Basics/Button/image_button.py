from tkinter import *
from PIL import ImageTk,Image
def resize_this(image,sizes):
    wow=(sizes[0],sizes[1])
    image=image.resize(wow,Image.ANTIALIAS)
    return image
root=Tk()
root.geometry('600x600')
rikka=(Image.open('Basics//Button//rikkalewd.jpg'))
rikka=resize_this(rikka,[200,100])
rikka=ImageTk.PhotoImage(rikka)
bt=Button(root,text='',width=200,height=100,image=rikka)
bt.place(x=20,y=20)
root.mainloop()
'''
? steps: 

1. copy the relative path and convert '/' to '//' and paste that in Image.open('here')
as usual use Image.open() and resize_this() and ImageTk().PhotoImage() in these Order
'''