# Solicita al usuario una cadena de caracteres
cadena = input("Ingrese una cadena de caracteres: ")

# Invierte la cadena utilizando la función reversed() y join()
cadena_al_reves = ''.join(reversed(cadena))

# Muestra la cadena al revés
print("Cadena al revés:", cadena_al_reves)
