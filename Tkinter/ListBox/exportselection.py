
# TODO: now the selection in one list box won't affect another
from tkinter import *
root=Tk()
lst1=Listbox(exportselection=0)
for i in range(10):
    lst1.insert(END,i)
lst2=Listbox(exportselection=0)
for i in range(10,20):
    lst2.insert(END,i)
lst3=Listbox(exportselection=0)
for i in range(20,30):
    lst3.insert(END,i)
lst1.pack()
lst2.pack()
lst3.pack()
root.mainloop()