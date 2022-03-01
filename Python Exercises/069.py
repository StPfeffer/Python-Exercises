def checkDivision(n):
    for i in range(0, n + 1):
        if i % 5 == 0 and i % 7 == 0:
            if i < n:
                print(i, end = ", ")
            else:
                print(i)


number = int(input("Enter a number: "))
checkDivision(number)

print()
print("Solution: ")


def divisible(n):
    i = 0
    while i <= n:
        if i % 5 == 0 and i % 7 == 0:
            yield i
        i += 1


n = int(input("Enter a number: "))
values = []
for i in divisible(n):
    values.append(str(i))

print(", ".join(values))
