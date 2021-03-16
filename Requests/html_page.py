import urllib.request

url = "https://www.google.co.in/"

test = urllib.request.urlopen(url)  # makes the GET request
# returns the source HTML code of the url
print(test.read())
