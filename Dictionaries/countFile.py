name = input("Enter file: ")

try:
    handle = open(name)
except:
    print(f"Cannot open file: {name}")
    quit()

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount) # most frequent word and the frequency total
