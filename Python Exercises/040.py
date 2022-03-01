from random import randrange


def printList():
    l = []

    for i in range(1, 21):
        l.append(i)

    return l[5:]


print(printList())
