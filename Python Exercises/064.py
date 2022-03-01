def calculate(n):
    result = 0.0

    if n > 0:
        for i in range(1, n + 1):
            result += float(i) / (i + 1)
    else:
        return 0

    return result


number = int(input("Enter a number: "))
print(calculate(number))
