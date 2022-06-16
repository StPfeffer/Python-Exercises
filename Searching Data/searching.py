handle = open("text.txt", "r", encoding = "UTF-8")

for line in handle:
    line = line.rstrip() # remove o "\n" da direita da frase, se não os outputs ficariam separados por 1 linha
    if line.startswith("Código"):
        print(line)

handle = open("text.txt", "r", encoding = "UTF-8")

for line in handle:
    line = line.rstrip() # remove o "\n" da direita da frase, se não os outputs ficariam separados por 1 linha
    if not line.startswith("Código"):
        continue
    print(line)
