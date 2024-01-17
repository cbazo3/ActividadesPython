class Cuenta:
    # Constructor de la clase
    def __init__(self, titular, cantidad=0.0):
        self.titular = titular  # I
        self.cantidad = cantidad  # I

    # Realizar un ingreso en la cuenta
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad  # Aumenta la cantidad si es un valor positivo

    # Realizar un retiro de la cuenta
    def retirar(self, cantidad):
        if cantidad > 0:
            if self.cantidad - cantidad < 0:
                self.cantidad = 0  # Establece la cantidad a cero si el retiro supera el saldo
            else:
                self.cantidad -= cantidad  # Realiza la retirada

    # Obtener la cantidad actual en la cuenta
    def get(self):
        return self.cantidad

    # Establecer una cantidad en la cuenta
    def set(self, cantidad):
        self.cantidad = cantidad

    # Obtener como cadena
    def toString(self):
        return f"Titular: {self.titular}, Cantidad: {self.cantidad}"

# Ejemplo de uso de la clase "Cuenta"
cuenta = Cuenta("Juan Pérez", 1000.0)  # Declaras que Juan tiene 1000€
print(cuenta.toString())  # Muestra los detalles de la cuenta

cuenta.ingresar(450.0)  # Realiza un ingreso en la cuenta
print("Después de ingresar 450 euros:", cuenta.toString())  # Muestra los detalles de la cuenta

cuenta.retirar(10.0)  # Realiza un retiro en la cuenta
print("Después de retirar 10 euros:", cuenta.toString())  # Muestra los detalles de la cuenta
