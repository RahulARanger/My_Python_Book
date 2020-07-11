import xml.etree.ElementTree as ET
hand=open('famil_num.xml')
data=''''''
for i in hand:
    data+=i+'''\n'''

tree=ET.fromstring(data)
lst=tree.findall('members/member')
print('The total members in my family is: ',len(lst))
for i in lst:
    print('Name: ',i.find('name').text)
    print('Phone Number: ',i.find('phone').text)
    print('\n')