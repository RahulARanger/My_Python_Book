from tkinter import *
class SearchBox(Frame):
    def __init__(self,parent,lst):
        super().__init__(parent)
        self.lst=lst
        self.var=StringVar()
        self.var.trace('w',self.track)
        self.Search=Entry(self,text='',textvariable=self.var,width=20)
        self.HBar=Scrollbar(self,orient=VERTICAL)
        self.lstbox=Listbox(self,yscrollcommand=self.HBar.set,height=10,width=20,exportselection=0)
        self.lstbox.bind('<Double-Button-1>',self.selected)
        self.Search.bind('<FocusIn>',self.appear)
        self.arrange()
    def appear(self,*arrgfs):
        self.HBar.pack(fill=Y,side=RIGHT)
        self.lstbox.pack()
    def track(self,*args):
        text=self.var.get()
        store=self.lstbox.get(0,END)
        for i in range(len(store)):
            self.lstbox.delete(0)
        if len(text)==0:
            for i in self.lst:
                self.lstbox.insert(END,i)
        else:
            for i in self.lst:
                if text in i:
                    self.lstbox.insert(END,i)    
    def arrange(self):
        self.Search.pack()
        for i in self.lst:
            self.lstbox.insert(END,i)
    def selected(self,*args):
        self.var.set(self.lstbox.get(ACTIVE))
        self.HBar.pack_forget()
        self.lstbox.pack_forget()
if __name__=='__main__':
    names=['Rahul','Kavita',"Srinivas",'Jignesh']
    root=Tk()
    a=SearchBox(root,names)
    a.pack()
    root.mainloop()
