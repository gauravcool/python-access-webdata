import re

data = 'From gaurav.ac.kumar@oracle.com Sat 17 09:12'

#Method 1: using find()
start = data.find('@')
end = data.find(' ', start)
pos = data[start+1 : end]
print(pos) #oracle.com

#Method 2: Double Split pattern
dataarr = data.split()
email = dataarr[1].split('@')
print(email[1]) #oracle.com

#Method 3: Regex
email2 = re.findall('@([^ ]*)', data)
print(email2) #['oracle.com']

email3 = re.findall('^From .*@([^ ]*)', data)
print(email3) #['oracle.com']
