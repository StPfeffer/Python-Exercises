def splitTuple():
    t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    # [int(len(t) / 2)] = midpoint of the list
    print(tuple(list(t)[:int(len(t) / 2)]))
    print(tuple(list(t)[int(len(t) / 2):]))


splitTuple()
