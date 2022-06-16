handle = open("text.txt", "r", encoding = "UTF-8")
print(handle)

count = 0

for line in handle:
    count += 1
    print(line)

print(f"Total lines: {count}")
