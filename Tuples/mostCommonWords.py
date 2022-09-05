fhand = open('text.txt', encoding='UTF-8')
counts = dict()

for line in fhand:
    words = line.split()

    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = list()

for (k, v) in counts.items():
    newtuple = (v, k)
    lst.append(newtuple)

lst = sorted(lst, reverse=True)

for v, k in lst[:10]: # apenas os 10 primeiros
    print(k, v)

# Shorter version for the 2nd for loop

c = { 'a': 10, 'b': 20, 'c': 1 }
print(sorted( [ (v, k) for (k, v) in c.items() ], reverse=True ))
