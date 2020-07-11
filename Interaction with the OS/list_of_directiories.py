import os
from tkinter import filedialog
path=filedialog.askdirectory()
print('The list of items inside in that location is:',os.listdir(path))