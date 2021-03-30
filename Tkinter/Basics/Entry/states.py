from tkinter import *
root=Tk()
def set_it(text):
    lb.config(state=text)
root.geometry('600x600')
lb=Entry(root,width=40)
lb.place(x=34,y=34)
disabled=Button(root,text='Disabled',command=lambda: set_it('disabled'))
normal=Button(root,text='Normal',command=lambda: set_it('normal'))
readonly=Button(root,text='Read Only',command=lambda:set_it('readonly'))
disabled.place(x=34,y=50)
normal.place(x=100,y=50)
readonly.place(x=160,y=50)
root.mainloop()