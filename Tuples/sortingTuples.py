# Sort by values

c = { 'a': 10, 'b': 1, 'c': 22 }
tmp = list()

for (k, v) in c.items():
    tmp.append((v, k))

print(tmp)
# [(10, 'a'), (1, 'b'), (22, 'c')]

tmp = sorted(tmp)
print(tmp)
# [(1, 'b'), (10, 'a'), (22, 'c')]