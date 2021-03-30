
from tkinter import *
from tkinter.ttk import* 
# Top level window 
window = Tk()

window.title("Studyfied.com")
window.geometry('350x200')

# Option menu variable
optionVar = StringVar()
optionVar.set("Red")

# Create a option menu
option = OptionMenu(window, optionVar, "Red", "Blue", "White", "Black")
option.pack()

# Create button with command
def show():
    print("Selected value :", optionVar.get())

btnShow = Button(window, text="Show", command=show)
btnShow.pack()

window.mainloop()