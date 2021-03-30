from tkinter import *
import threading
a=Tk()
w,h=300,300
a.geometry('300x300')
sw=a.winfo_screenwidth()
sh=a.winfo_screenheight()
# TODO: Here it is center positioned
to_x=int((sw-w)/2)
to_y=int((sh-h)/2)
print(w,h)
a.geometry('{}x{}+{}+{}'.format(w,h,to_x,to_y))
a.mainloop()