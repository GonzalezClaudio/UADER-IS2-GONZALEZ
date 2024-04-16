#------------------------------------------------------------------------------------------------------------------
# Trabajo Practico N° 4 - Patrones Estructurales.
# Gonzalez Claudio 
#------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------
# Punto 1:
# Provea una clase ping que luego de creada al ser invocada con un método 
# “execute(string)” realice 10 intentos de ping a la dirección IP contenida en 
# “string” (argumento pasado), la clase solo debe funcionar si la dirección IP 
# provista comienza con “192.”. Provea un método executefree(string) que haga 
# lo mismo pero sin el control de dirección. Ahora provea una clase pingproxy 
# cuyo método execute(string) si la dirección es “192.168.0.254” realice un ping a 
# www.google.com usando el método executefree de ping y re-envie a execute 
# de la clase ping en cualquier otro caso. (Modele la solución como un patrón proxy).
#------------------------------------------------------------------------------------------------------------------

# Patron de estructura proxy


from pythonping import ping
import os


# Clase Ping utilizando pythonping
class Ping:
    # Verifica si la direccion ip comienza con 192
    def execute(self, ip_address):
        if ip_address.startswith("192."):
            for _ in range(10):
                response = ping(ip_address, count=1)
                if response.success():
                    print(f"Ping exitoso a {ip_address}")
                else:
                    print(f"Ping fallido a {ip_address}")
        else:
            print("La dirección IP no comienza con '192.', ping no permitido.")

    def executefree(self, ip_address):
        for _ in range(10):
            response = ping(ip_address, count=1)
            if response.success():
                print(f"Ping exitoso a {ip_address}")
            else:
                print(f"Ping fallido a {ip_address}")

# La clase PingProxy actúa como un proxy para la clase Ping. 
# Si la dirección IP proporcionada es correcta, realiza un ping a "www.google.com" 
# utilizando el método executefree de la clase Ping, de lo contrario, 
# reenvía la solicitud a execute de la clase Ping.
class PingProxy:
    def __init__(self):
        self.ping = Ping()

    def execute(self, ip_address):
        if ip_address == "192.168.0.254":
            self.ping.executefree("www.google.com")
        else:
            self.ping.execute(ip_address)


#*------------------------------------------------------------
#* main
#*------------------------------------------------------------

os.system("cls")

ping_proxy = PingProxy()

# Ejecutando ping a una dirección que comienza con "192."
ping_proxy.execute("192.168.1.1")

# Ejecutando ping a una dirección que no comienza con "192."
ping_proxy.execute("10.0.0.1")

# Ejecutando ping a la dirección especial
ping_proxy.execute("192.168.0.254")


