# Solicita al usuario una cadena de caracteres
cadena = input("Ingrese una cadena de caracteres: ")

# Verifica si la cadena tiene al menos dos caracteres
if len(cadena) < 2:
    print("La cadena debe tener al menos dos caracteres para realizar el intercambio.")
else:
    # Intercambia el primer y último carácter
    nueva_cadena = cadena[-1] + cadena[1:-1] + cadena[0]
    
    # Muestra la nueva cadena
    print("Cadena con el primer y último carácter cambiados de posición:", nueva_cadena)
