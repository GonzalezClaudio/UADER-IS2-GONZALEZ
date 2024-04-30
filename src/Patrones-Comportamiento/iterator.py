#------------------------------------------------------------------------------------------------------------------
# Trabajo Practico N° 5 - Patrones de comportamiento.
# Gonzalez Claudio 
#------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------
# Punto 2:
# Implemente una clase bajo el patrón iterator que almacene una cadena de 
# caracteres y permita recorrerla en sentido directo y reverso.
#------------------------------------------------------------------------------------------------------------------

# Patron de comportamiento iterator

from __future__ import annotations
from collections.abc import Iterable
from typing import Any


class StringCollection(Iterable):
    """
    Concrete Collection class that stores a string and provides methods to iterate over it.
    """

    def __init__(self, string: str) -> None:
        self._string = string

    def __iter__(self) -> StringIterator:
        """
        The __iter__() method returns the iterator object itself for forward iteration.
        """
        return StringIterator(self._string)

    def get_reverse_iterator(self) -> StringIterator:
        """
        Returns an iterator for reverse iteration over the string.
        """
        return StringIterator(self._string, reverse=True)


class StringIterator:
    """
    Concrete Iterator for iterating over a string in both forward and reverse directions.
    """

    def __init__(self, string: str, reverse: bool = False) -> None:
        self._string = string
        self._index = len(string) - 1 if reverse else 0
        self._step = -1 if reverse else 1

    def __iter__(self) -> StringIterator:
        return self

    def __next__(self) -> str:
        """
        The __next__() method returns the next character in the string.
        On reaching the end, and in subsequent calls, it must raise StopIteration.
        """
        if 0 <= self._index < len(self._string):
            char = self._string[self._index]
            self._index += self._step
            return char
        else:
            raise StopIteration()


if __name__ == "__main__":
    # Uso de ejemplo
    string = "Hola mundo"

    # cadena original
    print("Cadena Directa:")
    for char in StringCollection(string):
        print(char, end="")
    print("\n")

    # cadena invertida
    print("Cadena invertida:")
    for char in StringCollection(string).get_reverse_iterator():
        print(char, end="")
    print("\n")
