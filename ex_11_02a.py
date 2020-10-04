import re
x = 'My 2 fav nos. are 56 and 45'
y = re.findall('[0-9]+', x)
print(y)
z = re.findall('[AEIOU]+', x)
print(z)
u = re.findall('[A-Za-z0-9]+', x)
print(u)