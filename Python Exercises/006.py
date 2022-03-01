from math import sqrt


c = 50
h = 30
value = []
items = [x for x in input("Enter a number or a series of numbers separated by a comma: ").split(",")]

for d in items:
    value.append(str(int(round(sqrt(2 * c * float(d) / h)))))

print(", ".join(value))
