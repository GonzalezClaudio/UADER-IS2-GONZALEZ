#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

#--------------------------------------------------------------------------
#Realice una modificación al programa para que si se omite el número como 
#argumento lo solicite. Pruebe.
#--------------------------------------------------------------------------- 

# Funcion para calcular el factorial de un número dado
#def factorial(num): 
#    if num < 0: 
#        print("El factorial de un número negativo no existe")
#        return None
#    elif num == 0: 
#        return 1
#    else: 
#        fact = 1
#        while(num > 1): 
#            fact *= num 
#            num -= 1
#        return fact 

#if len(sys.argv) != 2:
#    num_input = input("Por favor, ingrese un número para calcular su factorial: ")
#    try:
#        num = int(num_input)
#    except ValueError:
#        print("Debe ingresar un número válido.")
#        sys.exit()
#else:
#    num = int(sys.argv[1])

#print("El factorial de", num, "es", factorial(num))


#----------------------------------------------------------------------------------------------------
# Modifique el argumento (y el ingreso manual) para aceptar números en el rango desde-hasta (ej. 4-8) 
# y que calcule los factoriales entre ambos extremos. 
#----------------------------------------------------------------------------------------------------



# Funcion para calcular el factorial de un número dado
#def factorial(num): 
#    if num < 0: 
#        print("El factorial de un número negativo no existe")
#        return None
#    elif num == 0: 
#        return 1
#    else: 
#        fact = 1
#        while(num > 1): 
#            fact *= num 
#            num -= 1
#        return fact 

# Función para calcular los factoriales en un rango dado
#def calcular_factorial(desde, hasta):
#    for num in range(desde, hasta + 1):
#        print("El factorial de", num, "es", factorial(num))

#if len(sys.argv) != 2:
#    print("Para ingresar el rango utilice guion para separar los numeros. Ejemplo: (4-8)")
#    rango = input("Ingrese el rango de números al que desee calcular su factorial: ")
    
    # Divide la entrada en dos números (inicio y fin) utilizando el guion (-) como delimitador
#    desde, hasta = rango.split('-') 
    # Convierte los números de cadena a enteros
#    desde = int(desde)
#    hasta = int(hasta)
#else:
#    desde, hasta = sys.argv[1].split('-')
#    desde = int(desde)
#    hasta = int(hasta)

#calcular_factorial(desde, hasta) 


#----------------------------------------------------------------------------------------------------------
# Modifique el argumento (y el ingreso manual) para que acepte rangos sin límite inferior 
# “-hasta” calculando entre 1 y el número indicado (ejemplo “-10”), lo mismo para “desde-“ 
#calculando entre el número indicado y 60. Tenga la precaución de transformar las cadenas 
#de caracteres de la especificación de argumentos en valores enteros antes de intentar operaciones matemáticas. 
#-----------------------------------------------------------------------------------------------------------


# Funcion para calcular el factorial de un número dado



def factorial(num):
    if num < 0:
        print("El factorial de un número negativo no existe")
        return None
    elif num == 0:
        return 1
    else:
        fact = 1
        while num > 1:
            fact *= num
            num -= 1
        return fact

def calcular_factorial(desde, hasta):
    if desde <= hasta:  # Si el límite inferior es menor o igual al límite superior
        for num in range(desde, hasta + 1):
            print("El factorial de", num, "es", factorial(num))
    else:  # Si el límite inferior es mayor que el límite superior
        for num in range(desde, 0, -1):  # Calcular el factorial desde el límite superior hasta 1
            print("El factorial de", num, "es", factorial(num))

if len(sys.argv) != 2:
    print("Para ingresar el rango utilice guion para separar los numeros. Ejemplo: (-4) o (4-)")
    rango = input("Ingrese el rango de números al que desee calcular su factorial: ")
    
    # Verifica si el rango tiene un límite inferior especificado
    if '-' in rango:
        desde, hasta = rango.split('-')
        desde = int(desde) if desde else 1   # Si no se especifica el límite inferior, se establece en 1
        hasta = int(hasta) if hasta else 60  # Si no se especifica el límite superior, se establece en 60 

    else:
        desde = int(rango)
        hasta = 60  # Establece 60 como el límite superior predeterminado si no se especifica un límite superior
    
else:
    desde, hasta = sys.argv[1].split('-')
    desde = int(desde) if desde else 1   # Si no se especifica el límite inferior, se establece en 1
    hasta = int(hasta) if hasta else 60  # Si no se especifica el límite superior, se establece en 60

calcular_factorial(desde, hasta)




