import xml.etree.ElementTree as ET
import urllib.request
import ssl

#ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

urlInp = 'http://py4e-data.dr-chuck.net/comments_713342.xml'
print('Retrieving', urlInp)
url = urllib.request.urlopen(urlInp, context=ctx)
data = url.read()

commentinfo = ET.fromstring(data)
cmnts = commentinfo.findall('.//comment')
print('Count:', len(cmnts))
sum = 0

for item in cmnts:
    sum = sum + int(item.find('count').text)
print('Sum:', sum)