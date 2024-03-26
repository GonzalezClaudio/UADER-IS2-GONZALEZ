import matplotlib.pyplot as plt

def collatz(n):
    count = 0
    #Verifica si el numero(n) es divisible por 2 lo divide.
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        #En caso de que n sea impar lo multiplica por 3 y le suma 1
        else:
            n = 3 * n + 1
        count += 1   #contador de interacciones
    return count

def main():
    numeros = list(range(1, 1000)) # Le asigna la lista de numeros.
    iteraciones = [collatz(num) for num in numeros] #calcular el número de iteraciones de Collatz para cada número en la lista numeros.

    #Crea una nueva figura para el gráfico utilizando Matplotlib, le da el tamaño al cuadro
    plt.figure(figsize=(10, 6))
    #Realiza un grafico de dispersion con los datos de interacciones y numeros, con un punto de color rojo.     
    plt.scatter(iteraciones, numeros, marker='.', color='r')
    #Titulo del grafico
    plt.title('Número de Collatz para los números entre 1 y 1000')
    #Nombre del eje "X" 
    plt.xlabel('Iteraciones por cada número')
    #Nombre del eje "Y"
    plt.ylabel('Número de inicio de la secuencia (n)')
    #Cuadricula para visualizar mejor el gráfico
    plt.grid(True)
    #Muestra el gráfico
    plt.show()

if __name__ == "__main__":
    main()
