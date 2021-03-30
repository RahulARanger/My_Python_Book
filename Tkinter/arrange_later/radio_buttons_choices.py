from tkinter import *
root=Tk()
root['bg']='orange'
class choices:
    def __init__(self):
        self.choice=IntVar()
        self.check=0
        self.resu=StringVar()
        self.print_result=Label(root,textvariable=self.resu,bg='orange')
        self.apple=Radiobutton(root,text='Apple',bg='orange',variable=self.choice,value=1,command=self.check_apple)
        self.orange=Radiobutton(root,text='Orange',bg='orange',variable=self.choice,value=2,command=self.check_orange)
        self.banana=Radiobutton(root,text='Banana',bg='orange',variable=self.choice,value=3,command=self.check_banana)
    def result(self):
        if self.choice.get()==1:res='Apple'
        elif self.choice.get()==2:res='Orange'
        elif self.choice.get()==4:res=''
        else: res='Banana'
        self.resu.set('Your Favourite Fruit is  {}. '.format(res))
        
    def check_apple(self):
        print(self.choice.get(),self.check)
        if self.choice.get()==self.check :
            self.choice.set(4)
            self.check=0
        else:
            self.check=self.choice.get()
        self.result()    
    def check_orange(self):
        if self.choice.get()==self.check:
            self.choice.set(4)
            self.check=0
        else:
            self.check=self.choice.get()
        self.result()   
    def check_banana(self):
        if self.choice.get()==self.check:
            self.choice.set(4)
            self.check=0
        else:
            self.check=self.choice.get()                
        self.result()    
    def place_them(self):
        root.title('Choices')
        root.geometry('600x300')
        self.apple.place(x=200,y=150)
        self.orange.place(x=200,y=180)
        self.banana.place(x=200,y=210)
        self.print_result.place(x=200,y=230)
    def start_then(self):
        root.mainloop()      
a=choices()
a.place_them()
a.start_then()                  