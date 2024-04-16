from abc import ABC, abstractmethod

# Clase creator (Factura)
class Factura(ABC):
    @abstractmethod
    def calcular_importe(self, importe):
        pass


#*-----------------------------------------------------------------------
#* Es necesario hacer implementaciones concretas que reciban el objeto
#* plantilla y le agreguen los métodos y atributos que le sean propios
#*-----------------------------------------------------------------------
class FacturaResponsableIVA(Factura):
    def calcular_importe(self, importe):
        return importe * 1.24  # Aplica un 21% de IVA para Responsable Inscripto y un 3% de IIBB

class FacturaNoInscriptoIVA(Factura):
    def calcular_importe(self, importe):
        return importe * 1.03 # # Aplica un 3% de IIBB

class FacturaExentoIVA(Factura):
    def calcular_importe(self, importe):
        return importe  # No se aplica IVA para Exento

class FacturaFactory:
    def obtener_factura(self, tipo):
        if tipo == "Responsable":
            return FacturaResponsableIVA()
        elif tipo == "No Inscripto":
            return FacturaNoInscriptoIVA()
        elif tipo == "Exento":
            return FacturaExentoIVA()
        else:
            raise ValueError("Tipo de factura no válido")


#*-------------------------------------------------------------------------------
#* Este es el punto de entrada de ejecución (explicito)
#*-------------------------------------------------------------------------------
factory = FacturaFactory()

# Factura para Responsable Inscripto
factura_responsable = factory.obtener_factura("Responsable")
importe_responsable = 1000
print("Importe con IVA para Responsable Inscripto:", factura_responsable.calcular_importe(importe_responsable))

# Factura para No Inscripto
factura_no_inscripto = factory.obtener_factura("No Inscripto")
importe_no_inscripto = 1000
print("Importe sin IVA para No Inscripto:", factura_no_inscripto.calcular_importe(importe_no_inscripto))

# Factura para Exento
factura_exento = factory.obtener_factura("Exento")
importe_exento = 1000
print("Importe sin IVA para Exento:", factura_exento.calcular_importe(importe_exento))
