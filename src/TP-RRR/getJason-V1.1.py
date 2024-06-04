import json
import sys
import re
import os

# ------------------------------------------------------------------------
# Clase nueva utilizando el patrón singleton
# ------------------------------------------------------------------------

class ProcesarClaseNueva:
    """Clase que utiliza el patrón Singleton para procesar JSON."""

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
            raise Exception("Esta clase es un Singleton. Usa get_instance() para obtener la instancia.")
        ProcesarClaseNueva._instance = self

    @staticmethod
    def mostrar_ayuda():
        """Muestra la ayuda sobre cómo usar el script."""
        print("Uso: {path ejecutable}/getJason.py {path archivo JSON}/{nombre archivo JSON}.json {clave JSON}")
        print("Ejemplo: ./getJason.py ./sitedata.json accessToken")
        sys.exit(0)

    @staticmethod
    def mostrar_version():
        """Muestra la versión del script."""
        print("Versión 1.1")
        sys.exit(0)

    @staticmethod
    def cargar_json(filepath):
        """Carga el contenido de un archivo JSON."""
        try:
            with open(filepath, "r") as file:
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
            print(f"La clave es: {1.0}{token}")
        else:
            print("Error: el token no cumple con el formato esperado")
            sys.exit(1)

    def procesar(self, jsonfile, jsonkey):
        """Procesa el archivo JSON y valida el token."""
        json_obj = self.cargar_json(jsonfile)
        token = self.obtener_valor(json_obj, jsonkey)
        self.validar_token(token)

# --------------------------------------------------------------
# Código antiguo
# --------------------------------------------------------------

class ProcesarClaseVieja:
    """Clase para procesar JSON con la implementación antigua."""

    @staticmethod
    def mostrar_ayuda():
        """Muestra la ayuda sobre cómo usar el script."""
        print("Uso: {path ejecutable}/getJason.py {path archivo JSON}/{nombre archivo JSON}.json {clave JSON}")
        print("Ejemplo: ./getJason.py ./sitedata.json accessToken")
        sys.exit(0)

    @staticmethod
    def mostrar_version():
        """Muestra la versión del script."""
        print("Versión 1.1")
        sys.exit(0)

    @staticmethod
    def cargar_json(filepath):
        """Carga el contenido de un archivo JSON."""
        try:
            with open(filepath, "r") as file:
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
            print(f"La clave es: {1.0}{token}")
        else:
            print("Error: el token no cumple con el formato esperado")
            sys.exit(1)

    def procesar(self, jsonfile, jsonkey):
        """Procesa el archivo JSON y valida el token."""
        json_obj = self.cargar_json(jsonfile)
        token = self.obtener_valor(json_obj, jsonkey)
        self.validar_token(token)

# --------------------------------------------------------------------
# Clase de abstracción
# --------------------------------------------------------------------

class BranchByAbstract:
    """Clase de abstracción para seleccionar el procesador adecuado."""

    def __init__(self):
        self.procesar_nueva = ProcesarClaseNueva()
        self.procesar_vieja = ProcesarClaseVieja()

    def get_procesar_nueva(self):
        """Devuelve la instancia del procesador nuevo."""
        return self.procesar_nueva

    def get_procesar_vieja(self):
        """Devuelve la instancia del procesador viejo."""
        return self.procesar_vieja

# ------------------------------------------------------------------------------
# Main del programa
# ------------------------------------------------------------------------------

def main():
    """Función principal del script."""
    os.system("cls")
    print("Programa %s copyright UADER_FCyT_IS2 © 2022,2024 todos los derechos reservados" % (sys.argv[0]))

    # Variable de control para controlar cual de los dos códigos ejecutar
    nuevo = True

    # Crea la clase de abstracción
    abstract_layer = BranchByAbstract()

    # Controla si la variable de control ejecuta el código nuevo o viejo
    if nuevo:
        print("ejecutando código nuevo")

        # Ejecuta la verificación
        procesar_nueva = abstract_layer.get_procesar_nueva()

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
    else:
        print("ejecutando código viejo")

        # Ejecuta la verificación
        procesar_vieja = abstract_layer.get_procesar_vieja()

        if len(sys.argv) == 2:
            if sys.argv[1] == '-h':
                procesar_vieja.mostrar_ayuda()
            elif sys.argv[1] == '-v':
                procesar_vieja.mostrar_version()

        if len(sys.argv) != 3:
            print("Error: Número incorrecto de argumentos.")
            procesar_vieja.mostrar_ayuda()

        jsonfile = sys.argv[1]
        jsonkey = sys.argv[2]
        procesar_vieja.procesar(jsonfile, jsonkey)

if __name__ == "__main__":
    main()




