values = input("Enter a sequence of comma-separated numbers: ")
numbers = [x for x in values.split(",") if int(x) % 2 != 0]
print(", ".join(numbers))
