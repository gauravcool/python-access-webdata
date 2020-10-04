import xml.etree.ElementTree as ET

data = '''
<person>
    <name>Chuck</name>
    <phone type="international">+91 9964229574</phone>
    <email hide="yes"></email>
</person>
'''

tree = ET.fromstring(data)
print("Name: ", tree.find('name').text)
print('Attribute: ', tree.find('email').get('hide'))