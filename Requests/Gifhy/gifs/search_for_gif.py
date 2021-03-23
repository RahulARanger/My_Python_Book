import urllib.parse
import urllib.request
import json
import random


# api_key is only for testing purpose and the GIPHY doesnt recommend that for project
# that key is for the practice and it has certain limits per day
def search(search_for, results=1, mode=0, api_key="dc6zaTOxFJmzC"):
    # refer this for what this modes mean: https://developers.giphy.com/docs/api/schema#image-object
    modes = ['original', 'downsized', 'downsized_large',
             'downsized_medium', 'downsized_small', 'downsized_still',
             'fixed_height', 'fixed_height_downsampled', 'fixed_height_small',
             'fixed_height_small_still', 'fixed_height_still', 'fixed_width',
             'fixed_width_downsampled', 'fixed_width_small', 'fixed_width_small_still',
             'fixed_width_still', 'looping', 'original_still',
             'original_mp4', 'preview', 'preview_gif',
             'preview_webp', '480w_still'
             ]
    # mode = 0 (default) returns the original print (original upload)

    if mode > len(modes):
        return False

    url = "http://api.giphy.com/v1/gifs/search?"

    request_this = {
        "api_key": api_key,
        "limit": results,
        "q": search_for
    }

    with urllib.request.urlopen(url + urllib.parse.urlencode(request_this)) as rem_search_tht:
        if rem_search_tht.status != 200:
            return False
        store = json.loads(rem_search_tht.read().decode())["data"]

    if len(store) == 0:
        return False

    select_image = random.choice(range(results))

    return store[select_image]["images"][modes[mode]]["url"]


# this is for the testing purpose
if __name__ == "__main__":
    import webbrowser

    webbrowser.open(search("rem ova"))
