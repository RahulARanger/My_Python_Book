from tkinter import*
from tkinter import filedialog
e=Tk()
class editor:
    def __init__(self):
        self.enter=Text(e,width=72,height=30,bg='silver')
        self.saveas=Button(e,text='Save as',command=self.save_them)
    def place_them(self):
        self.enter.place(x=10,y=10)
        self.saveas.place(x=235,y=509)
    def save_them(self):
        text=self.enter.get(1.0,END)
        files = [('All Files', '*.*'),  
             ('Python Files', '*.py'), 
             ('Text Document', '*.txt')] 
        fil=filedialog.asksaveasfile(title='save them as',filetypes=files)
        fil.write(text)
        print(text)
    def start_them(self):
        e.title('Text Editor')
        e.geometry('600x600')               
        e.mainloop()

text=editor()
text.place_them()
text.start_them()
