class Matriz:
    # Constructor de la clase Matriz
    def __init__(self, rows, columns):
        # Inicializa los atributos rows y columns
        self.rows = rows
        self.columns = columns
        
        # Crea una matriz inicializada con ceros
        self.matrix = [[0] * columns for _ in range(rows)]

    # çObtener el número de filas
    def getNumberRows(self):
        return len(self.matrix)

    # Obtener el número de columnas
    def getNumberColumns(self):
        return len(self.matrix[0])

    # Establecer un elemento 
    def setElement(self, x, j, element):
        # Comprueba si las coordenadas son válidas
        if x < len(self.matrix) and j < len(self.matrix[0]):
            self.matrix[x][j] = element
        else:
            print("Hay un parámetro que no es válido.")

    # Método para sumar otra matriz a la matriz actual
    def addMatrix(self, m):
        # Comprueba si las dimensiones son compatibles
        if len(self.matrix) == len(m) and len(self.matrix[0]) == len(m[0]):
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    # Suma los elementos correspondientes
                    self.matrix[i][j] += m[i][j]
        else:
            print("La dimensión de las matrices es distinta la una de la otra.")

    # Método para multiplicar la matriz actual por otra matriz
    def multiMatrix(self, m):
        # Comprueba si las dimensiones son compatibles
        if len(self.matrix) == len(m) and len(self.matrix[0]) == len(m[0]):
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    # Multiplica los elementos correspondientes
                    self.matrix[i][j] *= m[i][j]
        else:
            print("La dimensión de las matrices es distinta.")

    # Método para representar la matriz como una cadena
    def __str__(self):
        return f"{self.matrix}"

# Crear una instancia de matriz1, tiene 3 filas y 3 columnas
matriz1 = Matriz(3, 3)

# Definir dos matrices
matriz2 = [[1, 3, 5], [2, 4, 6], [7, 8, 9]]
matriz3 = [[2, 5, 6], [4, 5, 7], [1, 2, 2]]

# Imprimir el número de filas y columnas de matriz1
print(matriz1.getNumberRows())
print(matriz1.getNumberColumns())

# Sumar matriz2 y matriz3 a matriz1
matriz1.addMatrix(matriz2)
matriz1.addMatrix(matriz3)

# Imprimir matriz1 después de la suma
print(matriz1)

# Multiplicar matriz1 por matriz2
matriz1.multiMatrix(matriz2)

# Imprimir matriz1 después de la multiplicación
print(matriz1)
