def printDictValues():
    d = dict()
    values = []
    for i in range(1, 21):
        d[i] = i ** 2
    
    for v in d.values():
        values.append(v)

    return values


print(printDictValues())

print()

def getValues():
    d = dict()

    for i in range(1, 21):
        d[i] = i ** 2
    
    return [v for v in d.values()]


print(getValues())
