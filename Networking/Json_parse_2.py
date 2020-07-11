import json
data=''''''
hand=open('family.json')
for i in hand:
    data+=i+'''\n'''
loaded=json.loads(data)
print('Total Members in my family: ',len(loaded))
print()
for i in range(len(loaded)):
    print('Name of the Person:',loaded[i]['member']['name'])
    print('Phone Number:',loaded[i]['member']['phone'])
    print()
