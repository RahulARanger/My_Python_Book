from tkinter import *
root=Tk()
e=Entry(root,fg='orange',bg='black')
e.place(x=300,y=260)
def print_it():
    
    display=Label(root,text=e.get())
    display.place(x=300,y=330)
    
root.geometry('600x600')
b=Button(root,text='Click me to know Abt tht!!!',command=print_it)
b.place(x=300,y=300)
root.mainloop()
