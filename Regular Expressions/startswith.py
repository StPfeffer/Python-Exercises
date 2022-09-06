# Using re.search() like startswith()

hand = open('text.txt', encoding='UTF-8')
for line in hand:
    line = line.strip()
    if line.startswith('From:'):
        print(line)


# Using regex:
import re


hand = open('text.txt', encoding='UTF-8')
for line in hand:
    line = line.strip()
    if re.search('^From:', line):
        print(line)
