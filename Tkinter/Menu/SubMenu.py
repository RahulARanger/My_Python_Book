from tkinter import*
root=Tk()
M=Menu(root)
# TODO: Above Menu is a simple Menu
submenu=Menu(M)
submenu.add_command(label='Hello',command=lambda :print('Hello'))
submenu.add_command(label='Hi',command=lambda :print('Hi'))
# TODO: here submenu is also the same as the Main ones
M.add_cascade(label='Greet',menu=submenu)
# * add_cascade adds a submenu to the Main ones
root.config(menu=M)
root.mainloop()