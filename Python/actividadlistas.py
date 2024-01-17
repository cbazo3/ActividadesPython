# Ruta completa del archivo romeo.txt
ruta_archivo = 'C:\\Users\\Usuario\\romeo.txt'

# Abre el archivo romeo.txt
with open(ruta_archivo, 'r') as archivo:
    # Inicializa una lista para almacenar las palabras únicas
    palabras_unicas = []

    # Lee el archivo línea por línea
    for linea in archivo:
        # Divide la línea en palabras usando el método split()
        palabras = linea.split()

        # Itera sobre cada palabra en la línea
        for palabra in palabras:
            # Verifica si la palabra ya está en la lista de palabras únicas
            if palabra not in palabras_unicas:
                # Agrega la palabra a la lista si no está presente
                palabras_unicas.append(palabra)

# Ordena la lista de palabras únicas
palabras_unicas.sort()

# Imprime la lista ordenada
print(palabras_unicas)
