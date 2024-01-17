def eliminar_repeticiones(lista):
    # Utiliza un conjunto para almacenar elementos únicos
    conjunto = set()
    resultado = []
    
    for elemento in lista:
        if elemento not in conjunto:
            conjunto.add(elemento)
            resultado.append(elemento)
    
    return resultado

# Ejemplo de uso
lista_ordenada = [1, 2, 2, 3, 3, 4, 4, 5, 5, 5, 1, 1]
resultado = eliminar_repeticiones(lista_ordenada)
print(resultado)
