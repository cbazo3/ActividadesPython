# Ruta completa del archivo media.txt
ruta_archivo = 'C:\\Users\\Usuario\\media.txt'

# Abre el archivo media.txt
with open(ruta_archivo, 'r') as archivo:
    # Inicializa el contador de correos electrónicos
    contador_correos = 0

    # Lee el archivo línea por línea
    for linea in archivo:
        # Verifica si la línea comienza con 'From ' y no 'From:'
        if linea.startswith('From ') and not linea.startswith('From:'):
            # Divide la línea en palabras usando el método split()
            palabras = linea.split()

            # Imprime la segunda palabra (la dirección de correo electrónico)
            if len(palabras) > 1:
                print(palabras[1])

            # Incrementa el contador de correos electrónicos
            contador_correos += 1

# Imprime el recuento al final
print(f"Recuento de correos electrónicos: {contador_correos}")
