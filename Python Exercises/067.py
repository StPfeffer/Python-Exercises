# f(0) = 0 if n = 0
# f(1) = 1 if n = 1
# f(n) = f(n - 1) + f(n - 2) if n > 1


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


number = int(input("Enter a number to see his fibonacci sequence: "))
values = [str(fib(x)) for x in range(0, number + 1)]
print(" → ".join(values))
