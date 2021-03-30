from tkinter import *
root=Tk()
b=StringVar()
b.set('c')
a=OptionMenu(root,b,'a','b','c')
a.pack()
root.mainloop()