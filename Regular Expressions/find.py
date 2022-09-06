# Using re.search() like find()

hand = open('text.txt', encoding='UTF-8')
for line in hand:
    line = line.strip()
    if line.find('From:') >= 0:
        print(line)


# Using regex:
import re


hand = open('text.txt', encoding='UTF-8')
for line in hand:
    line = line.strip()
    if re.search('From:', line):
        print(line)
