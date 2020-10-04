import re

handle = open('regex_sum_713338.txt')
numlist = list()
sum = 0
for line in handle:
    line = line.rstrip()
    stuff = re.findall('([0-9]+)', line)
    if len(stuff) < 1: continue
    res = list(map(int, stuff))
    print(res)
    for item in res:
        numlist.append(item)
for num in numlist:
    sum = sum + num
print(sum)