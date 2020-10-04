import urllib.request
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

counter = 0
url = input('Enter URL: ')
count = input('Enter count: ')
position_str = input('Enter position: ')
position = int(position_str) - 1
while (counter<int(count)):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    url = tags[position].get('href', None)
    counter = counter + 1
print(tags[position].contents[0])