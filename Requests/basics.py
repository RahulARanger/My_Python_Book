
import urllib.request

x = urllib.request.urlopen("https://www.google.co.in/")
print(x)
print(dir(x))
