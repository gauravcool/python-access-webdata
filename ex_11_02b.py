import re

x = 'From: gaurav: dshjhjdjh '
y = re.findall('^F.+?:', x)
print(y)

data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print('Atpos:', atpos)

sppos = data.find(' ', atpos)
print('Sppos:', sppos)

host = data[atpos+1 : sppos]
print('Host:', host)

words = data.split()
print(words)
line = words[1].split('@')
print(line[1])

z = re.findall('From .*@([^ ]*)', data)
print('Z:', z)