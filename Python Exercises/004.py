l = []

while True:
    number = int(input("Enter a number: "))
    l.append(number)
    answer = str(input("Do you want to enter another number [Y / N]: ")).strip().upper()[0]

    if answer == "N":
        break

print(l)
print(tuple(l))

print()

values = input("Enter a sequence of numbers separated by a comma: ")
l = values.split(",")
t = tuple(l)
print(l)
print(t)