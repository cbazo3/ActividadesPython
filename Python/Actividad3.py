import random
numero= random.randint (0, 20)
contador_intentos=0

print("¡Adivina el número entre 0 y 20!")
while True:
    try:
        numero_usuario = int(input("Ingrese un numero: "))
    except ValueError:
        print("¡Este no es el número secreto!")
        continue
    contador_intentos+=1

    if numero_usuario == numero:
        print("¡Has adivinado el número secreto!" + str(contador_intentos))
        break
    elif numero_usuario<numero:
        print("El número secreto es mayor")
    else:
        print("El número secreto es menor")
print("El juego ha acabado.")
