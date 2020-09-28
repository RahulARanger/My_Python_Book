from tkinter import *
root=Tk()
c=[1,2,3,4,5]
a=Listbox(root)
for i in c:
    a.insert(END,i)
a.pack()
root.mainloop()