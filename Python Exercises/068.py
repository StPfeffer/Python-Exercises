def printEvens(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            if i < n:
                print(i, end = ", ")
            else:
                print(i)


number = int(input("Enter a number: "))
printEvens(number)

print()
print("Solution: ")


def evenGenerator(n):
    i = 0
    while i <= n:
        if i % 2 == 0:
            yield i
        i += 1


n = int(input("Enter a number: "))
values = []

for i in evenGenerator(n):
    values.append(str(i))

print(", ".join(values))
