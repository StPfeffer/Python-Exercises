import re


hand = open('text.txt', encoding='UTF-8')
numlist = list()
for line in hand:
    line = line.strip()
    stuff = re.findall('^Código de segurança: ([0-9]+)', line)
    if len(stuff) != 1:
        continue
    numlist.append(stuff[0])
print('Maximum: ', max(numlist))
