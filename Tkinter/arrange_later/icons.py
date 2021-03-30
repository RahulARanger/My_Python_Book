from tkinter import *
root=Tk()
root.title('window with icon')
root.geometry('600x600')
# below command is for adding the icon to the window
root.wm_iconbitmap('google-ico.ico')
root.mainloop()