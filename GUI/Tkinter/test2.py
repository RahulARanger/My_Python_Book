from tkinter import *

root = Tk()
root.title("Steam Trader")
root.minsize(500, 800)
root.maxsize(500, 0)

menubar = Menu(root, background='#000099', foreground='white',
               activebackground='#004c99', activeforeground='white')
filemenu = Menu(menubar, tearoff=0, background='#000099',
foreground='white',
                activebackground='#004c99', activeforeground='white')
filemenu.add_command(label="Open", command=None)
filemenu.add_command(label="Save", command=None)
menubar.add_cascade(label="File", menu=filemenu)

root.config(bg='#2A2C2B', menu=menubar)
root.mainloop()