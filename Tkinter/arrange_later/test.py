from tkinter import *
from tkinter import ttk
root=Tk()
style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background="orange")

l1 = ttk.Label(root,text="Test", style="BW.TLabel")
l2 = ttk.Label(root,text="Test", style="BW.TLabel")
b1=ttk.Button(root,text='Test',style='BW.TButton')
l1.pack()
l2.pack()
b1.pack()
root.mainloop()