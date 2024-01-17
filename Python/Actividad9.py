# Definir el método indexContains que busca el valor en la tabla y devuelve su índice
# Si el valor no se encuentra, devuelve -1
def indexContains(tabla, cadena):
    for i, valor in enumerate(tabla):
        if valor == cadena:
            return i
    return -1

# Ejemplo de uso del método
tabla = ["cuervo", "periquito", "gorrión", "paloma", "loro"]
cadena = "loro"
indice = indexContains(tabla, cadena)

if indice != -1:
    print(f"'{cadena}' se encuentra en el índice {indice} de la tabla.")
else:
    print(f"'{cadena}' no se encuentra en la tabla.")
