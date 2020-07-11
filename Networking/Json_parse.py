import json
data='''
{
    "me":{
        "name":"Rahul",
        "phone":"91+ 8925071036"
    }
}'''
parsed=json.loads(data)
print("Name:",parsed["me"]["name"])
print("Phone Number:",parsed["me"]["phone"])