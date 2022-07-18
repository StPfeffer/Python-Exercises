data = "From stephen.marquard@utc.ac.za Sat Jan 5 09:14:16 2008"

posicao_arroba = data.find("@")
print(posicao_arroba)

posicao_espaco = data.find(" ", posicao_arroba)
print(posicao_espaco)

dominio = data[posicao_arroba + 1 : posicao_espaco]
print(dominio)
