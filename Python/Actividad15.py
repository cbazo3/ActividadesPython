nombre_archivo = "Actividad15.txt"
contenido_arcivo = "Holi teacher"

try:
    # Abrir el archivo o lo crea si no existe
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(contenido_arcivo)  # Escribe el contenido en el archivo

    # Imprime un mensaje como que todo  está bien
    print(f"El archivo '{nombre_archivo}' se ha creado exitosamente con el contenido: {contenido_arcivo}")

    # Lee el archivo sin espacios
    with open(nombre_archivo, 'r') as archivo:
        contenido_leido = archivo.read().replace(" ", "")  # Elimina los espacios

    # Imprime el contenido del archivo sin espacios
    print(f"Contenido del archivo sin espacios: {contenido_leido}")

except Exception as e:
    # Excepción por si ocurre un error
    print(f"Ocurrió un error: {str(e)}")
