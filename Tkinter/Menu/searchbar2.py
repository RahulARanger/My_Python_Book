from tkinter import *
# ! searchbar.py and this doesn't have any differences
class Test:
    def __init__(self,parent,parent2):
        self.parent=parent
        self.parent2=parent2
        self.store=[]
    def add_Them(self,text):
        self.store=list(set([i for i in text]))
    def showThem(self,event):
        self.menu=Menu(self.parent)
        self.menu.delete(0,END)
        for i in self.store:
            self.menu.add_command(label=i)  
        self.menu.post(event.x_root,event.y_root)
    def removeThem(self,event):
        try:self.menu.destroy()
        except:pass
class testing(Entry):
    def __init__(self,parent):
        super().__init__(parent)
        self.parent=parent
        self.var=StringVar()
        self.config(textvariable=self.var)
        self.Menu=Test(parent,self)
        self.var.trace('w',lambda x,y,z:self.Menu.add_Them(self.var.get()))
        self.bind('<Enter>',self.Menu.showThem)
        self.bind('<Leave>',self.Menu.removeThem)
    

root=Tk()
a=testing(root)
a.pack()
root.mainloop()