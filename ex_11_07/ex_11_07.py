import re
#file = input("Enter file")
handle = open('regex_sum_42.txt')
numlist = list()

for line in handle:
    line = line.rstrip()
    match = re.findall('[0-9]+', line)
    if match == []:
        continue
    numlist.append(match)
newlist = list ()
for item in numlist:
    newlist.append(int(item[0]))
print(newlist)
sum = 0
for item in newlist:
    sum = sum + item
print(sum)
print('The sum of the numerical elements in the file is:', sum)
