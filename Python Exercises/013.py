sentence = input("Write anything: ")

letters = 0
digits = 0

for i in sentence:
    if i in "abcdefghijklmnopqrstuvwxyz":
        letters += 1
    elif i in "0123456789":
        digits += 1

print(f"LETTERS: {letters}")
print(f"DIGITS: {digits}")

print()

s = input("Write anything: ")
d = {"DIGITS": 0, "LETTERS": 0}

for c in s:
    if c.isdigit():
        d["DIGITS"] += 1
    elif c.isalpha():
        d["LETTERS"] += 1
    else:
        pass

print(f"LETTERS: {d['LETTERS']}")
print(f"DIGITS: {d['DIGITS']}")