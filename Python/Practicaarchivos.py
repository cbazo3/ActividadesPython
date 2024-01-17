# Solicitar el nombre del archivo al usuario
nombre_archivo = input("Ingrese el nombre del archivo: ")

try:
    # Abrir el archivo
    with open(f'C:\\Users\\Usuario\\{nombre_archivo}', 'r') as archivo:
        # Inicializar variables
        total_confianza = 0
        count = 0

        # Leer cada línea del archivo
        for linea in archivo:
            # Buscar líneas que empiezan con 'X-DSPAM-Confidence:'
            if linea.startswith('X-DSPAM-Confidence:'):
                # Extraer el valor decimal de la línea
                valor_confianza = float(linea.split(':')[1])
                
                # Sumar el valor al total
                total_confianza += valor_confianza
                
                # Incrementar el contador
                count += 1

        # Calcular el promedio
        if count > 0:
            promedio_confianza = total_confianza / count
            print(f"Confianza promedio de spam: {promedio_confianza}")
        else:
            print("No se encontraron líneas con el formato especificado en el archivo.")

except FileNotFoundError:
    print(f"No se pudo encontrar el archivo: {nombre_archivo}")
except Exception as e:
    print(f"Ocurrió un error: {e}")
