from tkinter import *
root=Tk()
m=Menu(root,title='Menu')
new=Menu(m,tearoff=0,activebackground='skyblue')
new.add_command(label='test1')
new.add_command(label='test2')
new.add_command(label='test3')
new.add_command(label='test4')
new.add_separator()
new.add_command(label='test5')
m.add_cascade(label='New',menu=new)
new2=Menu(m,tearoff=0,activebackground='orange')
new2.add_command(label='test1')
new2.add_command(label='test2')
new2.add_command(label='test3')
new2.add_command(label='test4')
new2.add_separator()
new2.add_command(label='test5')
m.add_cascade(label='New2',menu=new2)

root.config(menu=m)
root.mainloop()