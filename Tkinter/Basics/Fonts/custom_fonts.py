
# * for downloading custom fonts I recommend  https://fonts.google.com/

import pyglet
from tkinter import font
# ? step 0: import pyglet module
# ! Note: This pyglet doesn't add this font permanently so they have to used along with the script
pyglet.font.add_file('Basics\Fonts\RussoOne-Regular.ttf')
# ? step 1: add the file path as above file must of format .ttf (font files)
from tkinter import *
root=Tk()
root.geometry('300x300')
# ? Step 3: as usual use the font.Font() constructor and name as exactly in font family and voila!!!
cust=font.Font(family='Russo One',size=23)
lb=Label(root,text='Customized Font',font=cust)
lb.place(x=34,y=45)
root.mainloop()