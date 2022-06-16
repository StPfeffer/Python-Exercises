file_name = input("Enter the file name: ")

try:
    handle = open(file_name, "r", encoding = "UTF-8")
except:
    print(f"File cannot be oppened: {file_name}")
    quit()

count = 0
for line in handle:
    if line.startswith("Código"):
        count += 1

print(f"There were {count} código lines in {file_name}")
