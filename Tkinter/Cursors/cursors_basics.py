from tkinter import *
root=Tk()
# TODO: Different cursor for the whole window (can only be inserted through config)
root.config(cursor='mouse')
root.geometry('600x600')
# TODO: Different cursor for the whole button
bt=Button(root,text='changed',width=30,height=10)
bt.config(cursor='dotbox')
bt.place(x=20,y=30)
root.mainloop()