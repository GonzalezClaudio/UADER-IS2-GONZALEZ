#------------------------------------------------------------------------------------------------------------------
# Trabajo Practico N° 3 - Patrones de Creacion.
# Gonzalez Claudio 
#------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------
# Punto 1:
# Provea una clase que dado un número entero cualquiera retorne el factorial del 
# mismo, debe asegurarse que todas las clases que lo invoquen utilicen la misma instancia de clase.
#------------------------------------------------------------------------------------------------------------------
# Patron de creacion singleton

# Clase singleton
import os

class CalcularFactorial:
    _instance = None

    # La clase __new__ la cree para asegurar de que siempre se retorne la misma instancia de la clase. 
    # Si la instancia aún no está creada, se crea una nueva instancia y se guarda en la variable de clase _instance

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
# El método calculate_factorial calcula el factorial de manera recursiva. 
    def factorial(self, n):
        if n < 0:
            raise ValueError("No pueden ser numeros negativos para el calculo de factorial")
        if n == 0:
            return 1
        return n * self.factorial(n - 1)


#*---- Este es el punto implícito de comienzo de ejecución

os.system('cls')

calcularfactorial = CalcularFactorial()
numero = int(input('Ingrese el numero al que deseas calcular su factorial'))
resultado = calcularfactorial.factorial(numero)
print(f"El factorial de {numero} es {resultado}")
