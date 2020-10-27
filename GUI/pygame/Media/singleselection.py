from tkinter import *
import os
from tkinter import filedialog
a=Tk()
b=filedialog.askopenfilenames(title='Open the Audio File',parent=a,initialdir=os.getcwd(),filetypes=(('Audio Files','.mp3'),))

print(b)
# ! b is empty if nothing is selected
a.mainloop()
