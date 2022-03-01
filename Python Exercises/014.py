sentence = input("Write anything: ")

uppers = 0
lowers = 0

for c in sentence:
    if c.isupper():
        uppers += 1
    elif c.islower():
        lowers += 1
    else:
        pass

print(f"UPPER CASE: {uppers}")
print(f"LOWER CASE: {lowers}")

print()

s = input("Wite anything: ")
d = {"LOWER": 0, "UPPER": 0}

for c in s:
    if c.isupper():
        d["UPPER"] += 1
    elif c.islower():
        d["LOWER"] += 1
    else:
        pass

print(f"UPPER: {d['UPPER']}")
print(f"LOWER: {d['LOWER']}")
