# ! __pre__ module contains some adjustments to the API 
import __pre__
import urllib
import pytube
import re
import os
import sys
bytes_to_mb=lambda x:(x/(10**6))

# ! adjustment line (important)
pytube.__main__.apply_descrambler = __pre__.apply_descrambler
class YTBackend:
    def __init__(self):
        self.options=[]
        pass
    def streams(self,yt,format,extension):
        self.all_streams=yt.streams
        self.display=[]
        if format is None and extension is None:
            # ! use this when user didn't check any filters
            pass
        if format is not None:
            if format=='videos':
                self.all_streams=yt.streams.filter(only_video=True)
            else:
                self.all_streams=yt.streams.filter(only_audio=True)
        for i in self.all_streams:
            element=[]
            element.append(i.itag)
            element.append(i.mime_type)
            element.append(i.type)
            element.append(bytes_to_mb(i.filesize))
            if i.type=='video':
                element.append(i.resolution)
            else:
                element.append(i.abr)
            self.display.append(element)
        # TODO: each element of the self.display is of the form
        # TODO: [itag,type,size,resolution/abr]
        print()
        print(self.display)
        print()
    def download(self,itag):
        selected=self.all_streams.get_by_itag(itag)
        # ! we can only select the folder path
        # * use save in folder widget from tkinter
        folder_path=input('Save in folder: ')
        selected.download(folder_path)

class YT(YTBackend):
    def __init__(self,link):
        super().__init__()
        self.Link=link
    def check(self):
        # ! Exception just in case to indicate the wrong links enterted
        try:
            self.yt=pytube.YouTube(self.Link)
        except:
            return False
        self.details()
        return True
    def details(self):
        self.Title=self.yt.title
        self.Desc=self.yt.description
        self.Rating=self.yt.rating
        self.Views=self.yt.views
        self.Length=self.yt.length
    def preview(self):
        # TODO: we will show the video thumbnail in the label to show the user about the video
        self.Thumbnail=self.yt.thumbnail_url
        # ? makes a temporary directory to store the thumbnail if not present 
        if 'temp' not in os.listdir(os.getcwd()):
            os.mkdir('temp')
        extension=re.findall(r'([.][a-z]+)',self.Thumbnail)[-1]
        file_path='temp/'+self.Title+extension
        self.cover=file_path
        urllib.request.urlretrieve(self.Thumbnail,file_path)
        # * download the image in that URL now
    def choices(self,format=None,extension=None):
        super().streams(self.yt,format,extension)

    def __del__(self):
        # create a way o delete the files inside the temp folder
        pass
if __name__=='__main__':
    link=input('Enter the link: ')
    a=YT(link)
    if a.check() is False:sys.exit(0)

    # TODO: we can use this videos as the details below the video preview tab
    print(a.Title) # ? returns the title of the video as the string
    #* print(a.Desc) # ? returns the string type of the description of youtube
    #* print(a.Rating) # ? returns the rating of the video in decimal (out of 5)
    # * print(a.Views) # ? returns the number of views of the video
    # * print(a.Length) # ? returns the length of the video in minutes
     # ? downloades the thumbnail of the video as the self.title.extension in temp folder
    a.choices()
    #a.choices('videos')
    #a.choices('audio')
    # ! with fronend make this through mouse clicks
    itag=input('Enter Your selection')
    a.download(itag)