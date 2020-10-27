import pytube
import __pre__
pytube.__main__.apply_descrambler = __pre__.apply_descrambler

link=input('Enter the Link: ')
a=pytube.YouTube(link)
# TODO: To Display the title of the yt video
print('Title:',a.title)
# TODO: Todisplay the description of the selected video
print()