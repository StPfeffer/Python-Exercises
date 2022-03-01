l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evenNumbers = [x for x in l if x % 2 == 0]

print(evenNumbers)

# Solução proposta utilizando o filter() não funciona mais!
"""
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evenNumbers = filter(lambda x: x % 2 == 0, l)
print(evenNumbers)
"""