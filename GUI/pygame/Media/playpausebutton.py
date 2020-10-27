import pygame
from tkinter import *
import os
from tkinter import filedialog
pygame.mixer.init()
root=Tk()
name=Label(root,text='Open Audio File')
def play_it():
    a=filedialog.askopenfilenames(title='Open the Audio File',initialdir=os.getcwd(),filetypes=(('Audio Files','.mp3'),))
    if len(a)==0:
        pass
    else:
        print(a)
        pygame.mixer.music.load(a[0])
        name.config(text='loaded music...')
        print('Music Time Length: ')
def play_music():
    pygame.mixer.music.play()
def stop_music():
    pygame.mixer.music.pause()



openbt=Button(root,text='Open',command=play_it)
playbt=Button(root,text='play',command=play_music)
pausebt=Button(root,text='pause',command=stop_music)
name.pack()
openbt.pack()
playbt.pack()
pausebt.pack()
root.mainloop()