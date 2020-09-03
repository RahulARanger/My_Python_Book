import json
import googletrans
store=googletrans.LANGUAGES
print(store)
with open('Json\Writing\languages_stored.json','w') as hand:
    json.dump(store,hand)
with open('Json\Writing\languages_stored.json','r') as hand:
    got=json.loads(hand.read())
    print(got)