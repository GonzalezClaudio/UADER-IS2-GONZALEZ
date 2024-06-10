Extractor de token para acceso API Servicios Banco XXX (versión 1.0)

Este programa permite extraer la clave de acceso API para utilizar los servicios del 
Banco XXX.

El programa operará como un microservicio invocado mediante:

        {path ejecutable}/getJason.pyc {path archivo JSON}/{nombre archivo JSON}.json

ej.
        ./getJason.pyc ./sitedata.json

El token podrá recuperarse mediante el standard output de ejecución en el formato

       {1.0}XXXX-XXXX-XXXX-XXXX

El cliente puede elegir con que banco realizar un pago, si esa cuenta no dispone de saldo suficiente
pasa a la siguiente cuenta, dicha transicion se controla con el patron cadena de comando.

Por cada pago que se realiza se almacena en una lista: con su correspondiente numero de pedido,
banco que se realiza el pago, el monto pagado y el saldo restante de dicha cuenta.

Para recorrer la lista de pagos se utiliza el patron interator.


Para obtener un mensaje de ayuda detallado ejecutar

       ./getJason.py -h

Para obtener un mensaje con la version del programa ejecutar

       ./getJason.py -v

Excepciones

Todas las condiciones de error del programa deben producir un mensaje de error bajo su control antes de
terminar.


