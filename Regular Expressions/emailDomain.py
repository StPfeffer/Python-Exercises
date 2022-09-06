import re


data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos) # 21
sppos = data.find(' ', atpos)
print(sppos) # 31
domain = data[atpos + 1: sppos]
print(domain) # uct.ac.za

# Double Split pattern

words = data.split()
email = words[1]
pieces = email.split('@')
print(pieces[1]) # uct.ac.za

# RegEx Version

y = re.findall('@([^ ]*)', data) # look through the string until
                                 # you find an '@', then match non-blank
                                 # character ([^ ])-many of them (*).
print(y) # ['uct.ac.za']

# Better RegEx Version

y = re.findall('^From .*@([^ ]*)', data)
print(y) # ['uct.ac.za']
