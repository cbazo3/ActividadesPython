def es_matriz_simetrica(matriz):
    # Comprueba que la matriz sea cuadrada
    if len(matriz) != len(matriz[0]):
        return False
    
    n = len(matriz)  # Tamaño de la matriz

    # Compara los elementos con sus elementos reflejados en la diagonal principal
    for i in range(n):
        for j in range(i, n):
            if matriz[i][j] != matriz[j][i]:
                return False

    return True

# Ejemplo de uso
matriz = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]

if es_matriz_simetrica(matriz):
    print("La matriz es simétrica")
else:
    print("La matriz no es simétrica")
