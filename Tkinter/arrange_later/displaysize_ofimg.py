from tkinter import *
from PIL import Image,ImageTk
root=Tk()
wow=Image.open('test.jpg')
wow=ImageTk.PhotoImage(wow)
button=Label(root,image=wow)
print(wow.height(),wow.width())
button.pack()
button.focus_set()
#root['image']=wow
root.mainloop()