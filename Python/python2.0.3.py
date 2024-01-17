# Función para añadir un elemento a la lista
def agregar_elemento(lista):
    elemento = int(input("Ingrese un número: "))
    lista.append(elemento)
    print("Elemento agregado a la lista.")

# Función para eliminar un elemento de la lista
def eliminar_elemento(lista):
    if len(lista) == 0:
        print("La lista está vacía.")
    else:
        elemento = int(input("Ingrese el número que desea eliminar: "))
        if elemento in lista:
            lista.remove(elemento)
            print(f"Elemento {elemento} eliminado de la lista.")
        else:
            print(f"El elemento {elemento} no está en la lista.")

# Función para listar el contenido de la lista
def listar_contenido(lista):
    if len(lista) == 0:
        print("La lista está vacía.")
    else:
        print("Contenido de la lista:")
        for elemento in lista:
            print(elemento)

# Función para contar las apariciones de un número en la lista
def contar_apariciones(lista):
    if len(lista) == 0:
        print("La lista está vacía.")
    else:
        elemento = int(input("Ingrese el número que desea contar: "))
        apariciones = lista.count(elemento)
        print(f"El número {elemento} aparece {apariciones} veces en la lista.")

# Función para calcular la media y el máximo de los elementos de la lista
def calcular_media_maximo(lista):
    if len(lista) == 0:
        print("La lista está vacía.")
    else:
        media = sum(lista) / len(lista)
        maximo = max(lista)
        print(f"Media de la lista: {media}")
        print(f"Valor máximo de la lista: {maximo}")

# Función principal
def main():
    lista = []
    
    while True:
        print("\nMenú:")
        print("1. Añadir un elemento a la lista")
        print("2. Eliminar un elemento de la lista")
        print("3. Listar el contenido")
        print("4. Contar las apariciones de un número en la lista")
        print("5. Calcular la media y el máximo de los elementos de la lista")
        print("0. Terminar")
        
        opcion = input("Ingrese una opción: ")
        
        if opcion == '1':
            agregar_elemento(lista)
        elif opcion == '2':
            eliminar_elemento(lista)
        elif opcion == '3':
            listar_contenido(lista)
        elif opcion == '4':
            contar_apariciones(lista)
        elif opcion == '5':
            calcular_media_maximo(lista)
        elif opcion == '0':
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida del menú.")

if __name__ == "__main__":
    main()
