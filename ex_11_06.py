import re
handle = open('mbox-short.txt')
numlist = list()

for line in handle:
    line = line.rstrip()
    stuff = re.findall('X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1:
        continue    
    num = float(stuff[0])
    #print(num)
    numlist.append(num)
print(max(numlist))

text = 'We just received $10.00 for shopping'
match = re.findall('\$[0-9.]+', text)
print(match) #['$10.00']

x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y) #['From: Using the :']
