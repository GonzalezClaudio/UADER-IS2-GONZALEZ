#------------------------------------------------------------------------------------------------------------------
# Trabajo Practico N° 3 - Patrones de Creacion.
# Gonzalez Claudio 
#------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------
# Punto 3:
# Genere una clase donde se instancie una comida rápida “hamburguesa” que pueda ser entregada en mostrador, 
# retirada por el cliente o enviada por delivery. A los efectos prácticos bastará que la clase imprima el método de 
# entrega.
#------------------------------------------------------------------------------------------------------------------

# Patron de creacion factory

from __future__ import annotations
from abc import ABC, abstractmethod
import os

#*--------------------------------------------------
#* La clase Creador es una superclase creadora de 
#* objetos donde las clases no están especificadas
#*--------------------------------------------------
class Creator(ABC):
    """
    La clase Creator declara la "factory" que retorna un puntero a un objeto
    pero que no tiene implementaciones concretas de sus métodos, es como 
    una plantilla de creación futura
    """

    @abstractmethod

    def factory_method(self):
        pass

#*----------------------------------------------------------------
#* Podría no crearlo pero también es posible implementar alguna
#* operación que sea común a todas las posibles implementaciones
#* esta lógica puede ser luego revertida al crear los objetos
#* operativos propiamente dichos
#*----------------------------------------------------------------
    def some_operation(self) -> str:

        print("{some_operation()}\n")
        # Primero se llama al método factory para crear un nuevo objeto hamburguesa.
        hamburguesa = self.factory_method()

        # A continuación uso el objeto creado invocando la operación específica para el mismo (que no figura definida en la clase que estoy usando).
        #result = f"Ejecución del Creator con {hamburguesa.operation()}\n"
        return "Detalle de retiro (%s)" %(hamburguesa.operation())


#*-----------------------------------------------------------------------
#* Es necesario hacer implementaciones concretas que reciban el objeto
#* plantilla y le agreguen los métodos y atributos que le sean propios
#*-----------------------------------------------------------------------

class CreatorEntregaMostrador(Creator):
    def factory_method(self) -> hamburguesa:
        return EntregaMostrador()


class CreatorEntregaCliente(Creator):
    def factory_method(self) -> hamburguesa:
        return EntregaCliente()

class CreatorEntregaDelivery(Creator):
    def factory_method(self) -> hamburguesa:
        return EntregaDelivery()


#*------------------------------------------------------------------------------
#* Defino al objeto Hamburguesa propiamente dicho
#*-----------------------------------------------------------------------------
class hamburguesa(ABC):

    #*-------------------------------------------------------------------------
    #* Esta es una interfaz que define todos los métodos que son comunes a 
    #* los remitos independientemente de como sean enviados
    #*-------------------------------------------------------------------------
    @abstractmethod
    def operation(self) -> str:
        pass


#*-------------------------------------------------------------------------------
#* Ahora defino hamburguesa con su respectiva definición de método de entrega
#*-------------------------------------------------------------------------------

class EntregaMostrador(hamburguesa):
    def operation(self) -> str:
        return "{Hamburguesa lista: Entrega en el mostrador}"


class EntregaCliente(hamburguesa):
    def operation(self) -> str:
        return "{Hamburguesa lista: Retira el cliente}"

class EntregaDelivery(hamburguesa):
    def operation(self) -> str:
        return "{Hamburguesa lista: Envio por delivery}"




#*-------------------------------------------------------------------------------
#* El código que orquesta empieza con una instancia del Creator (factory) sin
#* definiciones concretas y procede a crearle las subclases de implementación
#* que sean necesarias.
#*-------------------------------------------------------------------------------
def client_code(creator: Creator) -> None:

    print(f"Nueva hamburguesa:\n"
	  f"{creator.some_operation()}",end="")

#*-------------------------------------------------------------------------------
#* Este es el punto de entrada de ejecución (explicito)
#*-------------------------------------------------------------------------------
if __name__ == "__main__":

    os.system("cls")
    print("{%s}\n\n" % (__name__))

    print("Retiro por mostrador")
    client_code(CreatorEntregaMostrador())
    print("\n")

    print("Retira el cliente")
    client_code(CreatorEntregaCliente())
    print("\n")

    print("Envio por delivery")
    client_code(CreatorEntregaDelivery())
    print("\n")

    print("Retira el cliente")
    client_code(CreatorEntregaCliente())
    print("\n")

    







