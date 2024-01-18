# Ruta del archivo a leer
nombre_archivo = "C:\\Users\\Usuario\\media.txt"

try:
    # Abrir el archivo en modo de lectura ('r') usando el bloque 'with' para garantizar la correcta gestión de recursos
    with open(nombre_archivo, 'r') as archivo:
        # Inicializar un diccionario para almacenar la cantidad de correos enviados por cada remitente
        remitentes = dict()

        # Iterar sobre cada línea en el archivo
        for linea in archivo:
            # Verificar si la línea comienza con 'From '
            if linea.startswith('From '):
                # Dividir la línea en palabras y extraer la segunda palabra como la dirección del remitente
                palabras = linea.split()
                remitente = palabras[1]
                
                # Actualizar el diccionario de remitentes con la dirección del remitente y su conteo
                remitentes[remitente] = remitentes.get(remitente, 0) + 1

        # Verificar si hay remitentes en el diccionario
        if remitentes:
            # Encontrar la dirección del remitente que ha enviado la mayor cantidad de correos
            remitente_maximo = max(remitentes, key=remitentes.get)
            cantidad_maxima = remitentes[remitente_maximo]

            # Mostrar el resultado al usuario
            print(f"El remitente que ha enviado la mayor cantidad de correos es {remitente_maximo} con {cantidad_maxima} correos enviados.")
        else:
            # Mensaje en caso de no encontrar líneas 'From ' en el archivo
            print("No se encontraron líneas 'From ' en el archivo.")

except FileNotFoundError:
    # Mensaje en caso de no poder abrir el archivo debido a que no se encuentra
    print(f"No se pudo abrir el archivo {nombre_archivo}. Asegúrate de que la ruta del archivo sea correcta.")
except Exception as e:
    # Mensaje en caso de cualquier otro error durante la ejecución del programa
    print(f"Se produjo un error: {e}")
