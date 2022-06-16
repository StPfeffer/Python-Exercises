handle = open("text.txt", "r", encoding = "UTF-8")
whole_file = handle.read()

print(len(whole_file))
print(whole_file[:20])
print(f"\nWhole file:\n{whole_file}")
