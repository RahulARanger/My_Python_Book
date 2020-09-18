from tkinter import *
root=Tk()
root.geometry('600x600')
root.title('Frames')
frame=LabelFrame(root,text='Frame',width=100,height=100,bg='orange')
inside=Button(frame,text='Outside')
inside.place(x=0,y=0)
frame.place(x=300,y=200)
root.mainloop()