import json
import urllib.request
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

loc = input("Enter url: ")
url = urllib.request.urlopen(loc, context=ctx)
data = url.read().decode()
info = json.loads(data)
sum = 0
for item in info["comments"]:
    sum = sum + int(item["count"])
print(sum)