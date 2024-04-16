#------------------------------------------------------------------------------------------------------------------
# Trabajo Practico N° 4 - Patrones Estructurales.
# Gonzalez Claudio 
#------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------
# Punto 2:
# Para un producto láminas de acero de 0.5” de espesor y 1,5 metros de ancho 
# dispone de dos trenes laminadores, uno que genera planchas de 5 mts y otro 
# de 10 mts. Genere una clase que represente a las láminas en forma genérica al 
# cual se le pueda indicar que a que tren laminador se enviará a producir. (Use el 
# patrón bridge en la solución)
#------------------------------------------------------------------------------------------------------------------

# Patron de estructura bridge

from abc import ABC, abstractmethod

# Interfaz que actúa como el puente entre las láminas y los trenes laminadores
class Laminador(ABC):
    @abstractmethod
    def producir(self) -> None:
        pass

# Clase base para representar las láminas de acero
class HojaDeAcero:
    def __init__(self, espesor: float, ancho: float) -> None:
        self.espesor = espesor
        self.ancho = ancho

    def __str__(self) -> str:
        return f"Lámina de acero: Espesor {self.espesor} pulgadas, Ancho {self.ancho} metros"

# Clase para representar un tren laminador
class TrenLaminador:
    def __init__(self, laminador: Laminador) -> None:
        self.laminador = laminador

    def producir_chapa_acero(self) -> None:
        self.laminador.producir()


# Implementaciones concretas de la interfaz Laminator
class LaminadorDeCincoMetros(Laminador):
    def producir(self) -> None:
        print("Lámina producida por tren laminador de 5 metros.")

class LaminadorDeDiezMetros(Laminador):
    def producir(self) -> None:
        print("Lámina producida por tren laminador de 10 metros.")


# Ejemplo de uso
if __name__ == "__main__":
    hojaDeAcero = HojaDeAcero(espesor=0.5, ancho=1.5)

    laminador_cinco_metros = LaminadorDeCincoMetros()
    laminador_diez_metros = LaminadorDeDiezMetros()

    trenLaminador1 = TrenLaminador(laminador_cinco_metros)
    trenLaminador2 = TrenLaminador(laminador_diez_metros)

    print("Produciendo lámina de acero de 1.5 metros de ancho y 0.5 pulgadas de espesor...")
    print("Enviando al tren laminador de 5 metros:")
    trenLaminador1.producir_chapa_acero()

    print("\nEnviando al tren laminador de 10 metros:")
    trenLaminador2.producir_chapa_acero()
