phrase = [x for x in input("Enter a phrase: ").split(" ")]
frequency = []
words = {}

for w in phrase:
    words[w] = 1
    for i in frequency:
        if w == i:
            words[w] += 1
    frequency.append(w)

frequency = (dict(sorted(list(words.items()))))

for k, v in frequency.items():
    print(f"{k}: {v}")
