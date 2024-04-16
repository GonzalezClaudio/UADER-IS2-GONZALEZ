#------------------------------------------------------------------------------------------------------------------
# Trabajo Practico N° 4 - Patrones Estructurales.
# Gonzalez Claudio 
#------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------
# Punto 3:
# Represente la lista de piezas componentes de un ensamblado con sus 
# relaciones jerárquicas. Empiece con un producto principal formado por tres 
# sub-conjuntos los que a su vez tendrán cuatro piezas cada uno. Genere clases 
# que representen esa configuración y la muestren. Luego agregue un subconjunto opcional adicional también formado por cuatro piezas. (Use el patrón 
# composite).
#------------------------------------------------------------------------------------------------------------------

# Patron de estructura composite

from typing import List

# clase base que define la interfaz común para todas las clases que forman la estructura jerárquica.
class Componente:
    def mostrar(self, nivel: int) -> None:
        pass


# representa una pieza individual.
class Pieza(Componente):
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre

    def mostrar(self, nivel: int) -> None:
        print("  " * nivel + f"Pieza: {self.nombre}")

# representa un conjunto de piezas.
class Subconjunto(Componente):
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self.componentes: List[Componente] = []

    def agregar_componente(self, componente: Componente) -> None:
        self.componentes.append(componente)

    def mostrar(self, nivel: int) -> None:
        print("  " * nivel + f"Subconjunto: {self.nombre}")
        for componente in self.componentes:
            componente.mostrar(nivel + 1)

# Representa el producto principal que contiene varios subconjuntos.
class ProductoPrincipal(Componente):
    def __init__(self) -> None:
        self.subconjuntos: List[Componente] = []

    def agregar_subconjunto(self, subconjunto: Componente) -> None:
        self.subconjuntos.append(subconjunto)

    def mostrar(self, nivel: int) -> None:
        print("Producto Principal:")
        for subconjunto in self.subconjuntos:
            subconjunto.mostrar(nivel)

# Crear las piezas
piezas_subconjunto_1 = [Pieza(f"Pieza {i+1}") for i in range(4)]
piezas_subconjunto_2 = [Pieza(f"Pieza {i+5}") for i in range(4)]
piezas_subconjunto_3 = [Pieza(f"Pieza {i+9}") for i in range(4)]
piezas_subconjunto_opcional = [Pieza(f"Pieza {i+13}") for i in range(4)]

# Crear los subconjuntos
subconjunto_1 = Subconjunto("Subconjunto 1")
subconjunto_2 = Subconjunto("Subconjunto 2")
subconjunto_3 = Subconjunto("Subconjunto 3")
subconjunto_opcional = Subconjunto("subconjunto opcional")

# Agregar las piezas a los subconjuntos
for pieza in piezas_subconjunto_1:
    subconjunto_1.agregar_componente(pieza)

for pieza in piezas_subconjunto_2:
    subconjunto_2.agregar_componente(pieza)

for pieza in piezas_subconjunto_3:
    subconjunto_3.agregar_componente(pieza)

for pieza in piezas_subconjunto_opcional:
    subconjunto_opcional.agregar_componente(pieza)

#------------------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------------------

# Crear el producto principal
producto_principal = ProductoPrincipal()

# Agregar los subconjuntos al producto principal
producto_principal.agregar_subconjunto(subconjunto_1)
producto_principal.agregar_subconjunto(subconjunto_2)
producto_principal.agregar_subconjunto(subconjunto_3)
producto_principal.agregar_subconjunto(subconjunto_opcional)

# Mostrar la estructura del producto principal
producto_principal.mostrar(0)
