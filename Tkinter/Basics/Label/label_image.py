from tkinter import *
# ? step 0: import PIL package (especially ImageTk,Image)
from PIL import Image,ImageTk
# TODO: This resize_this will resize the image to sizes=[x,y] where x is new width and y is new height
def resize_this(image,sizes):
    wow=(sizes[0],sizes[1])
    image=image.resize(wow,Image.ANTIALIAS)
    return image
root=Tk()
root.geometry('1000x600')
# ? step:1 copy the relative path and paste it in Image.open('here') [note the '\\' characters for path indication]
rikka=Image.open('Basics\\Label\\rikkalewd.jpg')
# ? step 2: u can resize after opening it with Image.open()
# ? step 3: we can then open it using ImageTK.PhotoImage()
rikka=ImageTk.PhotoImage(rikka)
# ? step 4: now add it  in image attribute of the Label
lb=Label(text='',image=rikka)
lb.place(x=20,y=20)
rikka2=Image.open('Basics\\Label\\rikkalewd.jpg')
rikka2=resize_this(rikka2,[250,300])
rikka2=ImageTk.PhotoImage(rikka2)
# ! image is imposed over text by default
lb2=Label(text='Helsdsadsadsadsadasdasdlo there',image=rikka2)
lb2.place(x=650,y=0)
root.mainloop()