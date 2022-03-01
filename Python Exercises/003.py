def create_dict(n):
    d = dict()
    for i in range(1, n + 1):
        d[i] = i * i
    return d


number = int(input("Enter a number: "))
print(create_dict(number))