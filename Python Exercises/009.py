lines = []

while True:
    s = input("Write something: ")

    if s:
        lines.append(s.upper())
    else:
        break

for sentence in lines:
    print(sentence)
