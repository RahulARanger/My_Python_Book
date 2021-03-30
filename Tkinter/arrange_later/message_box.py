from tkinter import *
from tkinter import messagebox

root=Tk()
def display():
    a=messagebox.showinfo('messagebox','this is the info box')
    print(a)
    b=messagebox.showwarning('messagebox','this is the warning box')
    print(b)
    c=messagebox.showerror('message box','This is an error box')
    print(c)
    d=messagebox.askquestion('message box','asking question')
    print(d)  
    e=messagebox.askyesno('message box','yes or no')
    print(e)
    f=messagebox.askokcancel('message box','ok or cancel',default='cancel')
    print(f)
    g=messagebox.askyesnocancel('asdsad','gfh')
    print(g)
    
root.iconbitmap('google-ico.ico')
trigger=Button(root,text='Triggered',command=display)
trigger.pack()
root.mainloop()
