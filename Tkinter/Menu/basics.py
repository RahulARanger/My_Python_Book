
from tkinter import *
root=Tk()
m=Menu(root)
m.add_command(label='Hello',command=lambda :print('Hello'))
root.config(menu=m)
root.mainloop()