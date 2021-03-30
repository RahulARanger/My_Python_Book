from tkinter import*

root=Tk()
def action():
    label=Label(root,text='you Clicked me!!!')
    label.grid(row=6,column=6)
button=Button(root,text='Click me',command=action,bg='orange',activebackground='blue').grid(row=0,column=6)
root.mainloop()    