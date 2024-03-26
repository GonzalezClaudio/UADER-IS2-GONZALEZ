#------------------------------------------------------------------------------------------------------------------
#Genere un proyecto copia del anterior denominado “factorial_OOP” 
#donde tomando como base el programa “factorial.py” genere un programa “factorial_OOP.py” 
#donde se construya la lógica de cálculo de factorial mediante una clase Factorial 
#con un constructor y un método “run(min,max)” que calcule como resultado el factorial entre los números min y max.
#------------------------------------------------------------------------------------------------------------------

class Factorial:
    # Funcion para calcular el factorial de un número dado
    def factorial(self, num):
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

    def run(self, minimo, maximo):
        # Controla que el numero minimo del rango no puede ser mayor que el maximo
        if minimo > maximo:
            print("El número mínimo no puede ser mayor que el número máximo.")
            return
        for num in range(minimo, maximo + 1):
            print("El factorial de", num, "es", self.factorial(num))


if __name__ == "__main__":
    factorial_obj = Factorial()
    rango = input("Ingrese el rango, Ejemplo:(4-7): ")
    minimo, maximo = map(int, rango.split('-')) #La funcion map es para convertir la cadena en numeros enteros.
    factorial_obj.run(minimo, maximo)
