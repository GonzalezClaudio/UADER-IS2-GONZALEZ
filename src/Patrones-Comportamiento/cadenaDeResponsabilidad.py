#------------------------------------------------------------------------------------------------------------------
# Trabajo Practico N° 5 - Patrones de comportamiento.
# Gonzalez Claudio 
#------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------
# Punto 1:
# Cree una clase bajo el patrón cadena de responsabilidad donde los números del 
# 1 al 100 sean pasados a las clases subscriptas en secuencia, aquella que 
# identifique la necesidad de consumir el número lo hará y caso contrario lo 
# pasará al siguiente en la cadena. Implemente una clase que consuma números 
# primos y otra números pares. Puede ocurrir que un número no sea consumido 
# por ninguna clase en cuyo caso se marcará como no consumido.
#------------------------------------------------------------------------------------------------------------------

# Patron de comportamiento Chain of responsibility

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):
    """
    The Handler interface declares a method for building the chain of handlers.
    It also declares a method for executing a request.
    """

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    """
    The default chaining behavior can be implemented inside a base handler
    class.
    """

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)
        return ""


class PrimeHandler(AbstractHandler):
    def handle(self, request: int) -> str:
        result = ""
        if self._is_prime(request):
            result += f"PrimeHandler: Consume el numero primo {request}\n"
        # Llama a super para verificar si el numero es consumido por ambas cadenas.
        return result + super().handle(request)

    def _is_prime(self, n: int) -> bool:
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True


class EvenHandler(AbstractHandler):
    def handle(self, request: int) -> str:
        result = ""
        if self._is_even(request):
            result += f"EvenHandler: Consume el numero par {request}\n"
        # Llama a super para verificar si el numero es consumido por ambas cadenas.
        return result + super().handle(request) 

    def _is_even(self, n: int) -> bool:
        return n % 2 == 0


def client_code(handler: Handler) -> None:
    """
    The client code is usually suited to work with a single handler. In most
    cases, it is not even aware that the handler is part of a chain.
    """

    for number in range(1, 101):
        print(f"\nClient: Quien consume el numero {number}?")
        result = handler.handle(number)
        if result:
            print(result)
        else:
            print(f"  {number} No es consumido por ninguna cadena.")


if __name__ == "__main__":
    prime_handler = PrimeHandler()
    even_handler = EvenHandler()

    prime_handler.set_next(even_handler)

    print("Chain: PrimeHandler > EvenHandler\n")
    client_code(prime_handler)
    print("\n")




