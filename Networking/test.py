import json
with open('languages.json','r') as hand:
    a=json.loads(hand.read())
    print(a['Languages']['myanmar'])