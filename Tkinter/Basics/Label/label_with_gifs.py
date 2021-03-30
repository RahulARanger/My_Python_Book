from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.geometry('600x600')
rikka=Image.open('Basics\\Label\\tenor.gif')
rikka=ImageTk.PhotoImage(file=rikka,format="gif -index 2")
label=Label(root,text='Hello there',image=rikka)
label.place(x=23,y=34)
root.mainloop()