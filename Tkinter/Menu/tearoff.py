from tkinter import*
root=Tk()
M=Menu(root)

submenu=Menu(M)
submenu.add_command(label='Hello',command=lambda :print('Hello'))
submenu.add_command(label='Hi',command=lambda :print('Hi'))

submenu2=Menu(M,tearoff=0)
submenu2.add_command(label='Hello',command=lambda :print('Hello'))
submenu2.add_command(label='Hi',command=lambda :print('Hi'))

M.add_cascade(label='Greet with tearoff',menu=submenu)
M.add_cascade(label='Greet without tearoff',menu=submenu2)

root.config(menu=M)
root.mainloop()