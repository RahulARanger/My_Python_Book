from tkinter import *
import tkinter.ttk as ttk
root=Tk()
ae=['a','fsadgfsdgsdfgdsgsdfsfdsfdsfsdfsdsdsadsadsadsadasddfdsfsdfdsf','c']
a=ttk.Combobox(root,values=ae,state='readonly') # TODO readonly, disabled and normal
a.pack()
root.mainloop()