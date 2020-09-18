from tkinter import *
from tkinter import font
# TODO: Password entry will now show different symbol for the character typed
root=Tk()
def designs(en):
    en.config(borderwidth=3)
    en.config(background='#C9FFE5')
    en.config(foreground='#FF7E00')

root.geometry('500x300')
fo=font.Font(family='comic sans ms',size=23)
en=Entry(root,font=fo,justify='center')
designs(en)
password=Entry(root,font=fo,justify='left')
designs(password)
password.place(x=34,y=100)
password.config(show='*')
en.place(x=34,y=30)
root.mainloop()

