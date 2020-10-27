from tkinter import *
root=Tk()
m=Menu(root)
submenu=Menu(m,activebackground='orange',tearoff=0,title='testing Menu')

# ? accelerator is just a text shown on the right side of the menu
submenu.add_command(label='Hello',command=lambda :print('Hello'),activebackground='blue',accelerator='hi')
submenu.add_command(label='Hello',command=lambda :print('Hello'))
#? column break for the breaking the column of the menu
submenu.add_command(label='Hello',command=lambda :print('Hello'),columnbreak=True)
submenu.add_command(label='Hello',command=lambda :print('Hello'))
m.add_cascade(label='Test',menu=submenu)
root.config(menu=m)
root.mainloop()