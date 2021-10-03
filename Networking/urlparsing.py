import urllib.parse

website = input("Enter the website name: ")
tp = urllib.parse.urlparse(website)
print("The protocol used is: ", tp.scheme)
print("The server name is: ", tp.netloc)
print("The Location of the path of the webpage ", tp.path)
print("The URl of the given website: ", tp.geturl())
print("The Port number used is: ", tp.port)
print("all about the website is", tp)
