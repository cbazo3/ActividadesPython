def mayorYmenor(tabla):
    if not tabla:
        print("La tabla está vacía.")
        return

    # Inicializa las variables para el mayor y el menor
    mayor = menor = tabla[0]

    for cadena in tabla:
        if len(cadena) > len(mayor):
            mayor = cadena
        if len(cadena) < len(menor):
            menor = cadena

    print("String con mayor longitud:", mayor)
    print("String con menor longitud:", menor)

# Ejemplo de uso del método
tabla = ["cuervo", "periquito", "gorrión", "paloma", "loro", "golondrina"]
mayorYmenor(tabla)
