#------------------------------------------------------------------------------------------------------------------
# Trabajo Practico N° 4 - Patrones Estructurales.
# Gonzalez Claudio 
#------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------
# Punto 4:
# Implemente una clase que permita a un número cualquiera imprimir su valor, 
# luego agregarle sucesivamente.
#    a. Sumarle 2.
#    b. Multiplicarle por 2.
#    c. Dividirlo por 3.
# Mostrar los resultados de la clase sin agregados y con la invocación anidada a 
# las clases con las diferentes operaciones. Use un patrón decorator para implementar
#------------------------------------------------------------------------------------------------------------------

# Patron de estructura decorator


from abc import ABC, abstractmethod

# clase base que define la interfaz para representar un número y su método para imprimir su valor actual
class Numero(ABC):
    @abstractmethod
    def imprimir_valor(self) -> None:
        pass

# clase base para los decoradores de operación, que envolverán instancias de la clase Numero.
class OperacionDecorator(Numero):
    def __init__(self, numero: Numero) -> None:
        self._numero = numero

    def imprimir_valor(self) -> None:
        self._numero.imprimir_valor()

# Decorador para sumar 2 al número
class SumarDosDecorator(OperacionDecorator):
    def imprimir_valor(self) -> None:
        super().imprimir_valor()
        print(f" + 2 = {self._numero.valor + 2}")

# Decorador para multiplicar el número por 2
class MultiplicarPorDosDecorator(OperacionDecorator):
    def imprimir_valor(self) -> None:
        super().imprimir_valor()
        print(f" * 2 = {self._numero.valor * 2}")

# Decorador para dividir el número por 3
class DividirPorTresDecorator(OperacionDecorator):
    def imprimir_valor(self) -> None:
        super().imprimir_valor()
        print(f" / 3 = {self._numero.valor / 3}")

# Clase concreta para representar un número
class NumeroSimple(Numero):
    def __init__(self) -> None:
        self.valor = self._obtener_numero()

    def _obtener_numero(self) -> int:
        while True:
            try:
                valor = int(input("Ingrese un número (debe ser positivo y diferente de cero): "))
                if valor <= 0:
                    print("El número debe ser positivo y diferente de cero. Inténtelo de nuevo.")
                else:
                    return valor
            except ValueError:
                print("Por favor, ingrese un número entero válido.")

    def imprimir_valor(self) -> None:
        print(f"Número: {self.valor}")


if __name__ == "__main__":
    # Crear un número simple
    numero = NumeroSimple()
    numero.imprimir_valor()

    print("\nAplicando operaciones:")

    # Aplicar decoradores a la instancia original
    numero_sumar_dos = SumarDosDecorator(numero)
    numero_sumar_dos.imprimir_valor()

    numero_multiplicar_por_dos = MultiplicarPorDosDecorator(numero)
    numero_multiplicar_por_dos.imprimir_valor()

    numero_dividir_por_tres = DividirPorTresDecorator(numero)
    numero_dividir_por_tres.imprimir_valor()


