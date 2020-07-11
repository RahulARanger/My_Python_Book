from tkinter import *
def check(a):
    print(a)
root=Tk()
a=IntVar()
#b=IntVar()
r=Radiobutton(root,text='A',variable=a,value=1,command=lambda:check(a.get()))
re=Radiobutton(root,text='B',variable=a,value=2,command=lambda:check(a.get()))
r.place(x=10,y=15)
re.place(x=10,y=50)
root.mainloop()