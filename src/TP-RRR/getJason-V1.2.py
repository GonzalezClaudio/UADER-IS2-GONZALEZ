"""
Este módulo procesa archivos JSON y realiza pagos utilizando el patrón Singleton, 
Iterator y Chain of Responsibility.
"""
import json
import sys
import re
import os
from datetime import datetime

# ------------------------------------------------------------------------
# Clase nueva utilizando el patrón singleton
# ------------------------------------------------------------------------

class ProcesarClaseNueva:
    """
    Clase que utiliza el patrón Singleton para procesar JSON y realizar pagos.
    """

    _instance = None

    @staticmethod
    def get_instance():
        """Método estático para obtener la instancia única."""
        if ProcesarClaseNueva._instance is None:
            ProcesarClaseNueva()
        return ProcesarClaseNueva._instance

    def __init__(self):
        """Inicializador que controla la creación de una única instancia."""
        if ProcesarClaseNueva._instance is not None:
            raise RuntimeError("Esta clase es un Singleton. Usa get_instance() para obtener la instancia.")
        ProcesarClaseNueva._instance = self
        self.pagos_realizados = []

    @staticmethod
    def mostrar_ayuda():
        """Muestra la ayuda sobre cómo usar el script."""
        print("Uso: {path ejecutable}/getJason.py {path archivo JSON}/{nombre archivo JSON}.json {clave JSON}")
        print("Ejemplo: ./getJason.py ./sitedata.json accessToken")
        sys.exit(0)

    @staticmethod
    def mostrar_version():
        """Muestra la versión del script."""
        print("Versión 1.2")
        sys.exit(0)

    @staticmethod
    def cargar_json(filepath):
        """Carga el contenido de un archivo JSON."""
        try:
            with open(filepath, "r", encoding="utf-8") as file:  # "r" indica que el archivo se abre en modo de lectura
                return json.load(file)
        except FileNotFoundError:
            print("Error: archivo JSON no encontrado")
            sys.exit(1)
        except json.JSONDecodeError:
            print("Error: el archivo no es un JSON válido")
            sys.exit(1)

    @staticmethod
    def obtener_valor(json_obj, key):
        """Obtiene el valor asociado a una clave en el JSON."""
        try:
            return str(json_obj[key])
        except KeyError:
            print("Error: clave JSON no encontrada")
            sys.exit(1)

    @staticmethod
    def validar_token(token):
        """Valida el formato del token."""
        if re.match(r'^\w{4}-\w{4}-\w{4}-\w{4}$', token):
            return True
        print("Error: el token no cumple con el formato esperado")
        return False

    def procesar(self, jsonfile, jsonkey):
        """Procesa el archivo JSON, realiza el pago y registra el pago realizado."""
        json_obj = self.cargar_json(jsonfile)
        token = self.obtener_valor(json_obj, jsonkey)
        if not self.validar_token(token):
            sys.exit(1)
        self.pagos_realizados.append((datetime.now(), token))

    def registrar_pago(self, numero_pedido, token, monto, banco, saldo_restante):
        """Registra un pago realizado."""
        self.pagos_realizados.append((numero_pedido, token, monto, banco, saldo_restante))

    def listar_pagos(self):
        """Lista todos los pagos realizados por orden cronológico."""
        return PagosIterador(self.pagos_realizados)


# ------------------------------------------------------------------------
# Clase utilizando el patron iterator
# ------------------------------------------------------------------------

class PagosIterador:
    """Recorre la lista de los pagos realizados."""
    def __init__(self, pagos_realizados):
        self.pagos_realizados = pagos_realizados
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.pagos_realizados):
            pago = self.pagos_realizados[self.index]
            self.index += 1
            return pago
        raise StopIteration


# ------------------------------------------------------------------------
# Clase utilizando el patrón cadena de comando
# ------------------------------------------------------------------------

class Handler:
    """Clase base del manejador."""
    def __init__(self, saldo_inicial, nombre_banco, token=None):
        self.saldo = saldo_inicial
        self.nombre_banco = nombre_banco
        self.token = token
        self.siguiente = None

    def set_siguiente(self, handler):
        self.siguiente = handler

    def manejar(self, monto, numero_pedido, procesador):
        if self.puede_manejar(monto):
            self.realizar_pago(monto, numero_pedido, procesador)
        elif self.siguiente:
            self.siguiente.manejar(monto, numero_pedido, procesador)

    def puede_manejar(self, monto):
        return self.saldo >= monto

    def realizar_pago(self, monto, numero_pedido, procesador):
        self.saldo -= monto
        procesador.registrar_pago(numero_pedido, self.token, monto, self.nombre_banco, self.saldo)


class Banco1Handler(Handler):
    """Manejador para Banco1."""
    pass


class Banco2Handler(Handler):
    """Manejador para Banco2."""
    pass


# ----------------------------------------------------------------------------
# Main del programa
# ----------------------------------------------------------------------------

def main():
    """Función principal del programa."""
    os.system("cls")
    print(f"Programa {sys.argv[0]} copyright UADER_FCyT_IS2 © 2022,2024 todos los derechos reservados")

    # Ejecuta la verificación
    procesar_nueva = ProcesarClaseNueva.get_instance()

    # Verifica si se solicita el mensaje de ayuda o la versión
    if len(sys.argv) == 2:
        if sys.argv[1] == '-h':
            procesar_nueva.mostrar_ayuda()
        elif sys.argv[1] == '-v':
            procesar_nueva.mostrar_version()

    # Controla que si no se ingresa bien el argumento muestra el mensaje de cómo ingresarlo
    if len(sys.argv) != 3:
        print("Error: Número incorrecto de argumentos.")
        procesar_nueva.mostrar_ayuda()

    # Extrae la información para calcular desde los argumentos
    jsonfile = sys.argv[1]
    jsonkey = sys.argv[2]
    procesar_nueva.procesar(jsonfile, jsonkey)

    # Carga los datos del archivo JSON
    json_obj = ProcesarClaseNueva.cargar_json(jsonfile)

    # Obtiene los tokens del JSON
    token1 = json_obj.get("token1")
    token2 = json_obj.get("token2")

    if not token1 or not token2:
        print("Error: No se encontraron los tokens necesarios en el archivo JSON.")
        sys.exit(1)

    # Configura la cadena de responsabilidad
    banco1 = Banco1Handler(1000, "Banco1", token1)  # Saldo inicial $1000
    banco2 = Banco2Handler(2000, "Banco2", token2)  # Saldo inicial $2000

    banco1.set_siguiente(banco2)

    # Realiza pagos de ejemplo
    banco1.manejar(500, 1, procesar_nueva)    # Debe ser manejado por banco1
    banco1.manejar(500, 2, procesar_nueva)    # Debe ser manejado por banco1
    banco1.manejar(500, 3, procesar_nueva)    # Debe ser manejado por banco2
    banco1.manejar(500, 4, procesar_nueva)    # Debe ser manejado por banco2
    banco1.manejar(500, 5, procesar_nueva)    # Debe ser manejado por banco2
    banco1.manejar(500, 6, procesar_nueva)    # Debe ser manejado por banco2
    banco1.manejar(500, 7, procesar_nueva)    #  Error: No hay suficientes fondos en ninguna cuenta

    # Listar pagos realizados
    print("\nListado de pagos realizados:")
    for pago in procesar_nueva.listar_pagos():
        if len(pago) == 2:
            fecha, token = pago
            print(f"Fecha: {fecha}, Token utilizado para acceder: {token}")
        else:
            numero_pedido, token, monto, banco, saldo_restante = pago
            print(f"Pedido {numero_pedido}: Banco: {banco}, Monto a pagar: ${monto}, "
                  f"Token: {token}, Saldo restante: ${saldo_restante}")


if __name__ == "__main__":
    main()
    