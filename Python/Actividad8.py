# Definir el método sum que toma una lista de números y devuelve la suma
def sum(tabla):
    suma = 0
    for elemento in tabla:
        suma += elemento
    return suma

#Suma de los elementos de la tabla
tabla = [1, 2, 3, 4, 5]
resultado = sum(tabla)
print("La suma de los elementos en la tabla es:", resultado)
