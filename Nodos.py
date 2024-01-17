class NodoCola:
    def __init__(self, prenda):
    # Inicia el nodo con un dato (prenda) y hace la referencia al siguiente nodo (self.siguiente).
        self.prenda = prenda
        self.siguiente = None

class Cola:
    def __init__(self):
        # Inicia la cola con las referencias frente y final establecidas en una primera manera como None.
        self.frente = None
        self.final = None

    def encolar(self, nodo):
        # Agrega un nodo al final de la cola.
        # Si la cola está vacía, tanto frente como final apuntan al nuevo nodo.
        # Si no está vacía, el nodo se agrega al final y se actualiza la referencia final.
        if self.final is None:
            self.frente = nodo
            self.final = nodo
        else:
            self.final.siguiente = nodo
            self.final = nodo

    def desencolar(self):
        # Elimina el nodo del frente de la cola y devuelve el dato que se guarda en ese lugar (el primer lugar)
        # Si la cola está vacía, se imprime un mensaje y se devuelve None.
        if self.frente is None:
            print("La cola está vacía")
            return None
        else:
            prenda = self.frente.prenda
            self.frente = self.frente.siguiente
            if self.frente is None:
                self.final = None
            return prenda

    def imprimir_cola(self):
        # Imprime los datos de todos los nodos en la cola.
        actual = self.frente
        while actual is not None:
            print(actual.prenda, end=" ")
            actual = actual.siguiente
        print()

# Crear una cola de ropa
cola_ballet = Cola()

# Encolar algunos artículos
cola_ballet.encolar(NodoCola("Puntas")) #Este es el primer dato que entra
cola_ballet.encolar(NodoCola("Maillot"))
cola_ballet.encolar(NodoCola("Falda"))

# Imprimir la cola de ballet
print("Cola de ballet actual:")
cola_ballet.imprimir_cola()

# Desencolar una prenda
print("Artículo quitado de la cola:", cola_ballet.desencolar()) #el primero que entra por el primero que sale, desencolar quita de la cola lo primero que entra

# Imprimir la cola después de desencolar
print("Cola de ballet después de quitar la prenda de la cola:")
cola_ballet.imprimir_cola()
