import subprocess
from tkinter import filedialog
import os
file_name=filedialog.askopenfilename(title='Select Files',filetypes=[('Python Files','*.py')],initialdir=os.getcwd())
file_name='python '+'\"'+file_name+'\"'
print(file_name)
print(subprocess.check_output(file_name).decode())
# we can use os.system() function to run anotherprogram
