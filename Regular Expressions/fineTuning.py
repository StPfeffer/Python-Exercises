import re


x = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('\S+@\S+', x) # at least one non-whitespace character
print(y) # ['stephen.marquard@uct.ac.za']

# Parentheses tell where to start and stop what
# string to extract.

y = re.findall('^From (\S+@\S+', x)
print(y)
