import xml.etree.ElementTree as ET

input = '''
<stuff>
    <users>
        <user x="3">
            <name>Gaurav</name>
            <id>5121832</id>
        </user>
        <user x="5">
            <name>Kumar</name>
            <id>1pi10is034</id>
        </user>
    </users>
</stuff>
'''

stuff = ET.fromstring(input)
list = stuff.findall('users/user')
print('List length:', len(list))

for item in list:
    print('Name:', item.find('name').text)
    print('Id:', item.find('id').text)
    print('Attribute:', item.get('x'))