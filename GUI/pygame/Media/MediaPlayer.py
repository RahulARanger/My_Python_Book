import pygame
from tkinter import *
from tkinter import filedialog
import os
class MediaPlayer(Frame):
    def __init__(self,parent):
        super().__init__(parent)
        pygame.mixer.init()
        self.file=None
        self.opened=False
        self.started=False
        self.openit=Button(self,text='Open',command=self.getFile)
        self.openit.pack()
    def getFile(self):
        check=filedialog.askopenfilename(title='Open the Audio File',initialdir=os.getcwd(),filetypes=(('Audio Files','.mp3'),))
        if len(check)>0:
            self.file=check
            self.check_opened()
    def pauseIt(self):
        pygame.mixer.music.pause()
    def playIt(self):
        if not self.started:
            print('a)')
            pygame.mixer.music.play()
            print('a))')
            self.started=True
        else:pygame.mixer.music.unpause()
    def loadIt(self):
        
        pygame.mixer.music.load(self.file)
        print('The length:',pygame.mixer.music.get_pos())
    def check_opened(self):
        self.opened=True
        self.openit.destroy()
        self.loadIt()
        self.play=Button(self,text='Play',command=self.playIt)
        self.pause=Button(self,text='Pause',command=self.pauseIt)
        self.play.pack(side=LEFT)
        self.pause.pack(side=LEFT)
if __name__=='__main__':
    root= Tk()
    a=MediaPlayer(root)
    a.pack()
    root.mainloop()