#------------------------------------------------------------------------------------------------------------------
# Trabajo Practico N° 5 - Patrones de comportamiento.
# Gonzalez Claudio 
#------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------
# Punto 4:
# Modifique el programa IS2_taller_scanner.py para que además la secuencia de 
# barrido de radios que tiene incluya la sintonía de una serie de frecuencias 
# memorizadas tanto de AM como de FM. Las frecuencias estarán etiquetadas 
# como M1, M2, M3 y M4. Cada memoria podrá corresponder a una radio de AM 
# o de FM en sus respectivas frecuencias específicas. En cada ciclo de barrido se 
# barrerán las cuatro memorias.
#------------------------------------------------------------------------------------------------------------------

# Patron de comportamiento state
import os

class State:
    def scan(self):
        self.pos += 1
        if self.pos == len(self.stations):
            self.pos = 0
        print("Sintonizando... Estación {} {}".format(self.stations[self.pos], self.name))

class AmState(State):
    def __init__(self, radio):
        self.radio = radio
        self.stations = ["1250", "1380", "1510" , "1150"]
        self.memories = {"M1": "1250", "M2": "1380", "M3": "1510", "M4": "1150"}  # Frecuencias memorizadas para AM
        self.pos = 0
        self.name = "AM"

    def toggle_amfm(self):
        print("Cambiando a FM")
        self.radio.state = self.radio.fmstate

    def scan(self):
        super().scan()  # Escanea las estaciones normales
        print("Sintonizando... Memoria {} {}".format(self.memories["M1"], self.name))
        print("Sintonizando... Memoria {} {}".format(self.memories["M2"], self.name))
        print("Sintonizando... Memoria {} {}".format(self.memories["M3"], self.name))
        print("Sintonizando... Memoria {} {}".format(self.memories["M4"], self.name))

class FmState(State):
    def __init__(self, radio):
        self.radio = radio
        self.stations = ["81.3", "89.1", "103.9" , "107.1"]
        self.memories = {"M1": "81.3", "M2": "89.1", "M3": "103.9", "M4": "107.1" }  # Frecuencias memorizadas para FM
        self.pos = 0
        self.name = "FM"

    def toggle_amfm(self):
        print("Cambiando a AM")
        self.radio.state = self.radio.amstate

    def scan(self):
        super().scan()  # Escanea las estaciones normales
        print("Sintonizando... Memoria {} {}".format(self.memories["M1"], self.name))
        print("Sintonizando... Memoria {} {}".format(self.memories["M2"], self.name))
        print("Sintonizando... Memoria {} {}".format(self.memories["M3"], self.name))
        print("Sintonizando... Memoria {} {}".format(self.memories["M4"], self.name))

class Radio:
    def __init__(self):
        self.fmstate = FmState(self)
        self.amstate = AmState(self)
        self.state = self.fmstate  # Inicialmente en FM

    def toggle_amfm(self):
        self.state.toggle_amfm()

    def scan(self):
        self.state.scan()

if __name__ == "__main__":
    os.system("cls")
    print("\nCrea un objeto radio y almacena las siguientes acciones")
    radio = Radio()
    actions = [radio.scan] * 4 + [radio.toggle_amfm] + [radio.scan] * 4
    actions *= 2

    print("Recorre las acciones ejecutando la acción, el objeto cambia la interfaz según el estado")
    for action in actions:
        action()
