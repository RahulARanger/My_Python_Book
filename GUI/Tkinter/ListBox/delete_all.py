from tkinter import *
root=Tk()
a=Listbox(root)
def clear_it():
    note=a.get(0,END)
    print(note)
    for i in range(len(note)):
        a.delete(0)
def replace():
    clear_it()
    for i in range(10,20):
        a.insert(END,i)
for i in range(10):
    a.insert(END,i)
bt=Button(root,text='clear',command=clear_it)
bt1=Button(root,text='replace',command=replace)
a.pack()
bt.pack()
bt1.pack()
root.mainloop()