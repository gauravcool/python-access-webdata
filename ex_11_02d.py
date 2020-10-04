import re

numlist = list()

handle = open('mbox-short.txt')
for line in handle:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1: continue
    num = float(stuff[0])
    numlist.append(num)
print('Max:', max(numlist))