# Definir la tabla de salarios y empleados
salarios = [
    [700, 900, 1300],
    [1000, 950, 1080],
    [1300, 930, 1200]
]

empleados = ["Javier María", "Antonio Muñoz", "Isabel Allende"]

# Recorre las tablas y muestra la información
for i in range(len(empleados)):
    nombre = empleados[i]
    salario_trimestral = salarios[i]
    salario_anual = sum(salario_trimestral)  # Calcular el salario anual

    # Imprimir la información formateada
    print(f"{nombre} -> {salario_trimestral[0]} + {salario_trimestral[1]} + {salario_trimestral[2]} = {salario_anual}€")
