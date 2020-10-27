from tkinter import*
root=Tk()
menu=Menu(root)
menu.add_command(label='Hello',command=lambda :print('Hello'))
menu.add_command(label='Hi',command=lambda :print('Hi'))
# TODO: post method has the ability to create a popup menu
root.bind('<Button-3>',lambda x:menu.post(x.x_root,x.y_root))
root.mainloop()