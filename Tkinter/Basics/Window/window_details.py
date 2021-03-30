import threading
def check(a):
    print('The Width and Height is {}x{}'.format(a.winfo_width(),a.winfo_height()))
from tkinter import *
a=Tk()
a.geometry('600x600')
threading.Thread(target=check,args=(a,)).start()
a.mainloop()