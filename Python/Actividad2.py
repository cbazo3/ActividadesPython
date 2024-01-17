cantidadcero=0
cantidadmayorcero=0
cantidadmenorcero=0
for i in range (10):
    numero = int(input("Ingrese un numero: "))

    if numero == 0:
        cantidadcero +=1

    elif numero>0:
        cantidadmayorcero +=1

    else:
        cantidadmenorcero +=1

print("Cantidad de ceros introducidos:", cantidadcero)
print("Cantidad de numeros mayores de cero introducidos:", cantidadmayorcero)
print("Cantidad de numeros menores de cero introducidos:", cantidadmenorcero)