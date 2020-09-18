from tkinter import*
root=Tk()
already=0
def check():
    global already
    if already!=a.get():
        already=2
    else:
        a.set(0)
        already=0
a=IntVar()
rb=Radiobutton(root,variable=a,value=2,command=check)
rb.pack()
root.mainloop()