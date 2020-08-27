from tkinter import *
root=Tk()
# ! it seems we can't add border color to the button unless we change some internal settings (pain in the *ss)
def pressed(bt,bt2,n):
    if n==1 and bt['state']=='normal':
        bt.config(state='disabled',text='Not now',background='orange')
        bt2.config(state='active',text='Me',background='blue')
    else:
        bt2.config(state='disabled',text='Not now',background='orange')
        bt.config(state='active',text='Me',background='blue')
def designs(button):
    # ! refer refer_styles.png for different relief styles
    button.config(relief='solid')
    # TODO: borderwidth is responsible for the border in button
    button.config(borderwidth=10,background='blue')
root.geometry('600x600')
# ? anchor is related to the placed of the text inside the button
bt=Button(root,text='ME',width=10,height=10,anchor='center',command=lambda:pressed(bt,bt2,1))
bt.place(x=0,y=0)
designs(bt)
# * lambda : func_name(parameters) to call the function after pressing a button along with the arguments
bt2=Button(root,text='Me', width=10,height=10,anchor='center',command=lambda:pressed(bt,bt2,2))
bt2.place(x=510,y=0)
designs(bt2)
root.mainloop()