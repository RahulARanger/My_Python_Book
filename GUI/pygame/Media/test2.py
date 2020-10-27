import tkinter,tkinter.filedialog
from tkinter import messagebox

root = tkinter.Tk()
def main():
        files = tkinter.filedialog.askopenfilenames(parent=root,title='Choose files')
        msgbox = tkinter.messagebox.askquestion ('Add files','add extra files',icon = 'warning')
        return list(files), msgbox

files, msgbox = main()

all_files = files

while msgbox =='yes':
    files_2, msgbox = main()
    for i in files_2:
        files.append(i)
    
root.destroy()