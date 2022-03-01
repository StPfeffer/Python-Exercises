def getKeys():
    d = dict()

    for i in range(1, 21):
        d[i] = i ** 2

    return [k for k in d.keys()]


print(getKeys())
