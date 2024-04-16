#------------------------------------------------------------------------------------------------------------------
# Trabajo Practico N° 3 - Patrones de Creacion.
# Gonzalez Claudio 
#------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------
# Punto 2:
# Elabore una clase para el cálculo del valor de impuestos a ser utilizado por 
# todas las clases que necesiten realizarlo. El cálculo de impuestos simplificado 
# deberá recibir un valor de importe base imponible y deberá retornar la suma 
# del cálculo de IVA (21%), IIBB (5%) y Contribuciones municipales (1,2%) sobre 
# esa base imponible
#------------------------------------------------------------------------------------------------------------------
# Patron de creacion singleton

# Clase singleton
import os


class Impuestos:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def calcular_impuestos(self, precio_base):
        iva = precio_base * 0.21
        iibb = precio_base * 0.05
        contribuciones_municipales = precio_base * 0.012
        total_impuestos = iva + iibb + contribuciones_municipales
        return total_impuestos


#*---- Este es el punto implícito de comienzo de ejecución
os.system('cls')
impuestos = Impuestos()
precio_base = int(input("Ingrese el monto base imponible para calcular los impuestos: "))
total_impuestos = impuestos.calcular_impuestos(precio_base)
total_pagar = total_impuestos + precio_base
print(f"El total de impuestos a pagar es: {total_impuestos}")
print(f"Precio total con impuestos : {total_pagar}" )
