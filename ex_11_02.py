fname = input("Enter file name: ")
if len(fname) < 2 : fname = 'mbox-short.txt'
handle = open(fname)
for line in handle:
    line = line.rstrip()
    if line.startswith('From'):
        print(line)