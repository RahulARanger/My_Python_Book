import json
import urllib.request
import urllib.parse

url = "http://api.giphy.com/v1/gifs/search?"

post_this = {
    # basics
    "api_key": "dc6zaTOxFJmzC",
    "q": "Rem"

}

# made a post request by converting it to get request
with urllib.request.urlopen(url + urllib.parse.urlencode(post_this)) as rem_search_in_web:
    print(rem_search_in_web.geturl())
    store = json.loads(rem_search_in_web.read().decode())
