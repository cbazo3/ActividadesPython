# Definición de la función "n_p" para escribir números pares en un archivo "n_p.txt"
def n_p():
    # Abre el archivo txt
    with open("n_p.txt", "w") as archivo:
        for num in range(0, 101, 2):
            archivo.write(str(num) + "\n")  # Escribe números pares seguidos de un salto de línea

# Función para mostrar el contenido del txt
def mostrarArchivo():
    try:
        # Intenta abrir el archivo txt
        with open("n_p.txt", "r") as archivo:
            contenido = archivo.read()  
            print(contenido)  
    except FileNotFoundError:
        # Excepción si sale algún error
        print("No existe el archivo 'n_p.txt'. Prueba escribiendo antes los números pares.")

# Menú de opciones
while True:
    print("\nMenú:")
    print("1. Volcado de números pares en un archivo")
    print("2. Mostrar o leer el contenido del archivo")
    print("3. Salir del programa")
   
    numero = input("Selecciona una opción: ")
   
    if numero == "1":
        n_p()  # Llama a la función de la escritura de los números pares
    elif numero == "2":
        mostrarArchivo()  # Llama a la función para mostrar el contenido
    elif numero == "3":
        print("El programa finalizó.")
        break  # Sale del bucle
    else:
        print("Opción no válida. Debe seleccionar una opción válida (1, 2 o 3).")
