from tkinter import *

class Test(Menu):
    def __init__(self,parent,parent2):
        super().__init__(parent)
        self.parent2=parent2
    def add_Them(self,text):
        self.delete(0,END)
        chs=list(set([i for i in text]))
        for i in chs:
            self.add_command(label=i)       
    def showThem(self,event):
        self.post(event.x_root,event.y_root)
    

class testing(Entry):
    def __init__(self,parent):
        super().__init__(parent)
        self.parent=parent
        self.var=StringVar()
        self.config(textvariable=self.var)
        self.Menu=Test(parent,self)
        self.var.trace('w',lambda x,y,z:self.Menu.add_Them(self.var.get()))
        #self.bind('<Enter>',lambda x:self.Menu.add_Them(x,self.var.get()))
        self.bind('<Enter>',self.Menu.showThem)
        
    

root=Tk()
a=testing(root)
a.pack()
root.mainloop()