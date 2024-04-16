import os
#------------------------------------------------------------------------------------------------------------------
# Trabajo Practico N° 3 - Patrones de Creacion.
# Gonzalez Claudio 
#------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------
# Punto 5:
# Extienda el ejemplo visto en el taller en clase de forma que se pueda utilizar 
# para construir aviones en lugar de vehículos. Para simplificar suponga que un 
# avión tiene un “body”, 2 turbinas, 2 alas y un tren de aterrizaje.
#------------------------------------------------------------------------------------------------------------------


#*--------------------------------------------------------------------
#* La clase Director orquesta la construcción del objeto indicando 
#* el orden en que deben llamarse sus componentes, los mismos son
#* genéricos y dependerán del builder específico utilizado sus
#* valores concretos
#*--------------------------------------------------------------------
class Director:
    __builder = None
   
    def setBuilder(self, builder):
        self.__builder = builder
	   
    def getAirplane(self):
        airplane = Airplane()
      
        # Primero el cuerpo
        body = self.__builder.getBody()
        airplane.setBody(body)
      
        # Luego las turbinas
        i = 0
        while i < 2:
            turbine = self.__builder.getTurbine()
            airplane.attachTurbine(turbine)
            i += 1
      
        # Luego las alas
        i = 0
        while i < 2:
            wing = self.__builder.getWing()
            airplane.attachWing(wing)
            i += 1
      
        # Finalmente el tren de aterrizaje
        landing_gear = self.__builder.getLandingGear()
        airplane.setLandingGear(landing_gear)

        # Retorna el avión completo
        return airplane

#*----------------------------------------------------------------
#* Esta es la definición de un objeto vehiculo inicializando 
#* todos sus atributos
#*----------------------------------------------------------------
class Airplane:
    def __init__(self):
        self.__turbines = list()
        self.__wings = list()
        self.__body = None
        self.__landing_gear = None

    def setBody(self, body):
        self.__body = body

    def attachTurbine(self, turbine):
        self.__turbines.append(turbine)

    def attachWing(self, wing):
        self.__wings.append(wing)

    def setLandingGear(self, landing_gear):
        self.__landing_gear = landing_gear

    def specification(self):
        print("Cuerpo: %s" % (self.__body.shape))
        print("Turbinas: %d" % len(self.__turbines))
        print("Alas: %d" % len(self.__wings))
        print("Tren de aterrizaje: %s" % (self.__landing_gear.type))


#*-----------------------------------------------------------------
#* Builder
#* Clase genérica que solo define la interfaz de los métodos que el
#* Builder específico tiene que implementar
#*-----------------------------------------------------------------
class Builder:
    def getTurbine(self): pass
    def getWing(self): pass
    def getBody(self): pass
    def getLandingGear(self): pass


#*-----------------------------------------------------------------
#* Esta es la hoja de ruta para construir un Avion
#* Establece instancias para tomar body, alas, turbinas y tren de aterrizaje
#* estableciendo las partes específicas que (en un avion) 
#* deben tener esas partes
#*-------------------------------------------------------
class AirplaneBuilder(Builder):
    def getTurbine(self):
        turbine = Turbine()
        return turbine

    def getWing(self):
        wing = Wing()
        return wing

    def getBody(self):
        body = Body()
        body.shape = "Avión"
        return body

    def getLandingGear(self):
        landing_gear = LandingGear()
        landing_gear.type = "Ruedas"
        return landing_gear


#*----------------------------------------------------------------
#* Define partes genéricas para un Avion (sin inicializar)
#*----------------------------------------------------------------
class Turbine:
    pass

class Wing:
    pass

class Body:
    shape = None

class LandingGear:
    type = None



#*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
#* Esta es la estructura main()
#*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
def main():
    
    
    #*----------------------------------------------------------------
    #* Instancia la clase que será el resultado y la que guiará el 
    #* proceso de construcción
    #*----------------------------------------------------------------
    airplane_builder = AirplaneBuilder()
    director = Director()
    #*----------------------------------------------------------------
    #* Pasa al director la hoja de ruta para construir un avion
    #*----------------------------------------------------------------    
    director.setBuilder(airplane_builder)
    #*----------------------------------------------------------------
    #* Ordena al director agregar los componentes de un avion según
    #* la hoja de ruta
    #*----------------------------------------------------------------    
    airplane = director.getAirplane()
    #*---------------------------------------------------------------
    #* Finalizada la construcción verifica que sea completa
    #*---------------------------------------------------------------    
    airplane.specification()
    print("\n\n")

#*----------------------------------------------------------------------
#* Se detecta el entry point y se lo deriva a una sección main() propia
#*----------------------------------------------------------------------
if __name__ == "__main__":
    os.system("cls")
    print("Ejemplo de un patrón de tipo builder aplicado a la construcción de un avión\n")
    main()
