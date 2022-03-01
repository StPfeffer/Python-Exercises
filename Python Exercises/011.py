value = []
numbers = [number for number in input("Enter a sequence of comma separated 4 digit binary numbers: ").split(",")]

for i in numbers:
    int_i = int(i, 2)
    if not int_i % 5:
        value.append(i)

print(", ".join(value))
