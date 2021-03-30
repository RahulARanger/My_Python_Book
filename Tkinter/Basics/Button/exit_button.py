from tkinter import*
from PIL import ImageTk, Image
root=Tk()
root.geometry('600x600')
quit_me=Button(root,text='X',command=root.quit)
f=Image.open('exit.ico')
cross=ImageTk.PhotoImage(f)
quit_me.config(image=cross)
print(type(cross))
quit_me.place(x=80,y=90)
root.mainloop()