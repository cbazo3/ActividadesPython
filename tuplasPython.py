# Ruta donde se va a enconrtar el archivo a leer
nombre_archivo = "C:\\Users\\Usuario\\media-3.txt"

try:
    # Archivo en modo de lectura ('r'), usa el bloque 'with' para garantizar la gestión de los recursos
    with open(nombre_archivo, 'r') as archivo:
        # Inicializar un diccionario para almacenar la distribución por hora del día
        horas = dict()

        # Iterar sobre cada línea en el archivo
        for linea in archivo:
            # Verificar si la línea comienza con 'From '
            if linea.startswith('From '):
                # Dividir la línea para obtener la hora (separada por dos puntos) y extraer la hora en formato de 24 horas
                palabras = linea.split()
                hora = palabras[5].split(':')[0]

                # Actualizar el diccionario de horas con la hora y su conteo
                horas[hora] = horas.get(hora, 0) + 1

        # Ordenar el diccionario por hora e imprimir los resultados
        for hora, conteo in sorted(horas.items()):
            print(f"{hora} {conteo}")

except FileNotFoundError:
    # Mensaje en caso de no poder abrir el archivo debido a que no se encuentra
    print(f"No se pudo abrir el archivo {nombre_archivo}. Asegúrate de que la ruta del archivo sea correcta.")
except Exception as e:
    # Mensaje en caso de cualquier otro error durante la ejecución del programa
    print(f"Se produjo un error: {e}")
