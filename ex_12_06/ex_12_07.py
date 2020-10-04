import urllib.request
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
html_url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'

#url = input('Enter URL:')
#count = input('Enter count:')
countInit = 0
counts = dict()

while (countInit < 4):
    html = urllib.request.urlopen(html_url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    #print(tags)
    for tag in tags:
        url = tag.get('href').split()
        count = url
    print(count)
    countInit = countInit + 1
    print(url[0])
    html_url = url[0]
    