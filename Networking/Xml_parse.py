import xml.etree.ElementTree as ET

data = '''<me>
<name>Rahul</name>
<phone type="intl">91+ 8925071036</phone>
</me>'''
tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Phone Number:',tree.find('phone').text) 