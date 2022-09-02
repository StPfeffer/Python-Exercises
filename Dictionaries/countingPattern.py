counts = dict()

print("Enter a line of text: ")
line = input('')

words = line.split()

for word in words:
    counts[word] = counts.get(word, 0) + 1

print('Counts', counts)


print("\n\n")

jjj = { 'chuck': 1, 'fred': 42, 'jan': 100}
for k, v in jjj.items():
    print(k, v)
