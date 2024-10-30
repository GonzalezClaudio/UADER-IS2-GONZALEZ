# Calculando el número de iteraciones del algoritmo de Collatz
def collatz(num):
    # Contador de iteraciones
    iteraciones = 0  
    while num != 1:
        # Condición para números pares
        if num % 2 == 0:  
            num = num // 2
        # Condicion para numeros impares
        else:
            num = 3 * num + 1
        iteraciones += 1
    return iteraciones

# Solicitar y aceptar un número entero positivo por teclado
def main():
    # Solicitar al usuario un número y validarlo
    try:
        num = int(input("Ingrese un número entero positivo (máximo 1999 y minimo 1): "))
        if num < 1 or num > 1999:
            print("Error: El número debe estar entre 1 y 1999.")
            return
    except ValueError:
        print("Error: Debe ingresar un número entero válido.")
        return

    # Calcular iteraciones y mostrar resultados
    iteraciones = collatz(num)
    print("El número de iteraciones para llegar a 1 desde %d es %d." % (num, iteraciones))


if __name__ == "__main__":
    main()
