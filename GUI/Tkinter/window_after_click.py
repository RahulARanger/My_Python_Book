from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.title('Main Window')
a=Image.open('test.jpg')
def clicked():
    top=Toplevel()
    global a,img
    top.title('This is the sub-window')
    a.resize((200,200),Image.ANTIALIAS)
    img=ImageTk.PhotoImage(a)
    la=Label(top,image=img)
    la.pack()

bt=Button(root,text='Click to view image',command=clicked)
bt.pack()
root.mainloop()    