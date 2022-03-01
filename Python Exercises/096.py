def countCharacters(s):
    d = dict()

    for c in s:
        d[c] = d.get(c, 0) + 1
    
    return d


chars = countCharacters(input("Enter something: "))
print("\n".join(["%s, %s" % (k, v) for k, v in chars.items()]))
