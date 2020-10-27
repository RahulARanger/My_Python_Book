import pytube
import __pre__
# ! Due to some changes we have to apply some manual changes
pytube.__main__.apply_descrambler = __pre__.apply_descrambler
# TODO: Create the YouTube() object
link=input('Enter the Link: ')
a=pytube.YouTube(link)
print(a)
print(a.title)