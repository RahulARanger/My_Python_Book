from tkinter import filedialog
from tkinter import *
import os
a =  filedialog.askopenfilename(initialdir = os.getcwd(),title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
print(a)