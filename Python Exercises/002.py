def factorial(n):
    temp = 1
    if n == 0:
        return 1
    else:
        for i in range(n, 0, -1):
            temp *= i
        return temp


number = int(input("Enter a number to see his factorial: "))
result = factorial(number)
print(result)

print()


def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)


x = int(input("Enter a number to see his factorial: "))
print(fact(x))