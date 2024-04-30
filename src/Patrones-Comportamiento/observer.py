from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
import itertools
import random

class Subject(ABC):
    """
    The Subject interface declares a set of methods for managing subscribers.
    """

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Attach an observer to the subject.
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Detach an observer from the subject.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Notify all observers about an event.
        """
        pass


class ConcreteSubject(Subject):
    _state: str = None
    _observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:
        print("\nSubject: I'm emitting an ID.")
        cables_combinations = ['ABCD', 'EFGH', 'WXYZ', '1234', '5678', '9ABC', 'DEFG', 'HIJK']  # Lista de 8 claves posibles
        random.shuffle(cables_combinations)  # Mezcla aleatoriamente las claves
        selected_cables = random.sample(cables_combinations, k=4)  # Selecciona aleatoriamente 4 claves
        for cable in selected_cables:
            self._state = cable
            print(f"\nSubject: ID emitted: {self._state}")
            self.notify()

    def get_id(self) -> str:
        return self._state




class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, subject: Subject) -> None:
        """
        Receive update from subject.
        """
        pass


class ConcreteObserver(Observer):
    def __init__(self, observer_id: str):
        self._observer_id = observer_id

    


class ConcreteObserverA(ConcreteObserver):
    def __init__(self):
        super().__init__("ABCD")

    def update(self, subject: Subject) -> None:
        emitted_id = subject.get_id()
        if emitted_id == self._observer_id:
            print(f"Observer A: Received a matching ID")


class ConcreteObserverB(ConcreteObserver):
    def __init__(self):
        super().__init__("EFGH")

    def update(self, subject: Subject) -> None:
        emitted_id = subject.get_id()
        if emitted_id == self._observer_id:
            print(f"Observer B: Received a matching ID")


class ConcreteObserverC(ConcreteObserver):
    def __init__(self):
        super().__init__("WXYZ")

    def update(self, subject: Subject) -> None:
        emitted_id = subject.get_id()
        if emitted_id == self._observer_id:
            print(f"Observer C: Received a matching ID")


class ConcreteObserverD(ConcreteObserver):
    def __init__(self):
        super().__init__("1234")

    def update(self, subject: Subject) -> None:
        emitted_id = subject.get_id()
        if emitted_id == self._observer_id:
            print(f"Observer D: Received a matching ID")

        


if __name__ == "__main__":
    # El código del cliente.
    subject = ConcreteSubject()

    observer_a = ConcreteObserverA()
    subject.attach(observer_a)

    observer_b = ConcreteObserverB()
    subject.attach(observer_b)

    observer_c = ConcreteObserverC()
    subject.attach(observer_c)

    observer_d = ConcreteObserverD()
    subject.attach(observer_d)

    # Emitir 4 IDs seleccionadas aleatoriamente de las 8 posibles
    subject.some_business_logic()