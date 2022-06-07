def polygonArea(X, Y, n):
  
    # Inicia a área inicial
    area = 0.0
  
    # Calcula o valor da fórmula de shoelace
    j = n - 1
    for i in range(0, n):
        area += (X[j] + X[i]) * (Y[j] - Y[i])
        j = i   # j é o vértice anterior a i
      
  
    # Retorna o valor absoluto
    return int(abs(area / 2.0))
  
# programa para testar a função acima
X = [0, 2, 4]
Y = [1, 3, 7]
n = len(X)

print(polygonArea(X, Y, n))
