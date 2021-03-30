from tkinter import *
from PIL import Image,ImageTk
viewer=Tk()
viewer['bg']='#FF8C00'
viewer.geometry('600x600')
def resize_this(image,sizes):
    wow=(sizes[0],sizes[1])
    image=image.resize(wow,Image.ANTIALIAS)
    return image
class images:
    def __init__(self):
        self.set_them()
        self.lst_of_images=['image_viewer\\images\\1.jpg','image_viewer\\images\\2.jpg','image_viewer\\images\\3.jpg','image_viewer\\images\\4.jpg','image_viewer\\images\\5.jpg','image_viewer\\images\\6.jpg','image_viewer\\images\\7.jpg','image_viewer\\images\\8.jpg','image_viewer\\images\\9.jpg']
        self.pointer=0 
        self.status_bar()
    def reflect(self,code):
        print(self.pointer)
        if code=='l':
            if self.pointer==0:
                self.back.config(state=DISABLED)
            else:
                self.pointer-=1                
                self.front.config(state=NORMAL)
        else:
            if self.pointer==len(self.lst_of_images)-1:
                self.front.config(state=DISABLED)
            else:
                self.pointer+=1
                self.back.config(state=NORMAL) 
        self.choose=self.lst_of_images[self.pointer]
        self.img1=Image.open(self.choose)
        self.img1=resize_this(self.img1,[550,450])
        self.img1=ImageTk.PhotoImage(self.img1)
        self.place_them(self.img1)
        self.status_bar()
    def pointers(self):
        self.back=Button(viewer,text='<<',bd=6,bg='orange',command=lambda:self.reflect('l'),state=DISABLED)
        self.front=Button(viewer,text='>>',bd=6,bg='orange',command=lambda:self.reflect('r'))
    def set_them(self):
        self.pointers()
        self.back.config(width=10,height=2)
        self.front.config(width=10,height=2)
        self.back.place(x=100,y=500)
        self.front.place(x=400,y=500)
        self.img1=Image.open('image_viewer\\images\\1.jpg')
        self.img1=resize_this(self.img1,[550,450])
        self.img1=ImageTk.PhotoImage(self.img1)
        self.place_them(self.img1)
    def place_them(self,wow):
        self.display_place=Label(viewer,image=wow,relief=SOLID)
        self.display_place.config(width=550,height=450)
        self.display_place.place(x=20,y=20) 
        
    def status_bar(self):
        self.msg='{} of {} images   '.format(self.pointer+1,len(self.lst_of_images))
        self.status=Label(viewer,text=self.msg,bg='grey',relief=SUNKEN,borderwidth=3,anchor='e')
        self.status.config(width=85,height=2)
        self.status.place(x=0,y=563)    
a=images()
viewer.mainloop()