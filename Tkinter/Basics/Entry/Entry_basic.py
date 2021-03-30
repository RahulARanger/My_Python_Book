from tkinter import *
root=Tk()
check=0
def action(text_):
    lb=Label(root)
    lb.set(' '*check)
    lb.place(x=20,y=80)
root.geometry('600x600')
a=Entry(root)
a.place(x=20,y=20)
bt=Button(root,text='Print',command=lambda :action(a.get()))
bt.place(x=20,y=40)
root.mainloop()