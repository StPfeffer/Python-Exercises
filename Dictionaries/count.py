from itertools import count


counts = dict()
names = ['csve', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] += 1
print(counts)

# The pattern of checking to see if a key is already in a
# dictionary and assuming a default value if the key is not
# there is so common that there is a method called get() that
# does this for us.

counts = dict()
names = ['csve', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)
