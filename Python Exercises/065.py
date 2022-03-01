# n > 0
# f(n) = f(n - 1) + 100
# f(0) = 1


def calculate(n):
    if n < 0:
        return -1
    elif n != 0:
        # f(n) = f(n - 1) + 100
        return calculate(n - 1) + 100
    elif n == 0:
        return 0
    else:
        pass


number = int(input("Enter a number: "))
print(calculate(number))
