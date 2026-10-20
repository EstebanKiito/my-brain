---
ramo: "Sistemas Distribuidos"
tema: "Invocación remota"
tags:
  - sd/invocacion-remota
  - python
  - origen/complemento
prerrequisitos:
  - "[[02 - RPC y stubs]]"
---

# RPC y RMI en Python con xmlrpc

La biblioteca estándar de Python trae una implementación completa de RPC: `xmlrpc`, que serializa las llamadas en XML y las envía por HTTP. Con pocas líneas se publica un conjunto de funciones (o los métodos de un objeto, al estilo RMI) y se las llama desde otro proceso como si fueran locales.

## Servidor: registrar funciones

![Servidor RPC con SimpleXMLRPCServer](adjuntos/Servidor%20RPC%20con%20SimpleXMLRPCServer.png)

> [!example]- Transcripción de la imagen
> ```python
> DATA = []
>
> def f1(x, y):
>     return x + y
>
> def f2():
>     return "Hello World"
>
> def f3(x):
>     DATA.append(x)
>     return DATA[0]
> ```
> ```python
> from xmlrpc.server import SimpleXMLRPCServer
>
> ip_port = ("localhost", 4444)
> server = SimpleXMLRPCServer(ip_port, allow_none=True)
> server.register_function(f1, "add")
> server.register_function(f2, "hello_world")
> server.register_function(f3, "append")
> server.serve_forever()
> ```

- Las funciones son Python normal: no saben que se llamarán remotamente.
- `register_function(f, "nombre")` las publica con el nombre que verá el cliente (`f1` se llama `add` desde afuera).
- `allow_none=True` permite enviar y recibir `None`, que XML-RPC estándar no soporta.
- `serve_forever()` deja el servidor atendiendo peticiones; el **server stub** es el propio `SimpleXMLRPCServer`.

## Cliente: llamar como si fuera local

![Cliente RPC con ServerProxy](adjuntos/Cliente%20RPC%20con%20ServerProxy.png)

> [!example]- Transcripción de la imagen
> ```python
> from xmlrpc.client import ServerProxy
>
> servidor = ServerProxy("http://localhost:4444/", allow_none=True)
> print("3 + 8 =", servidor.add(3, 8))
> print("-->", servidor.hello_world())
> print("DATA: ", servidor.append("Probando"))
> print("DATA: ", servidor.append("4444"))
> print("Concatenar string: ", servidor.add("AN", "YA"))
> print("DATA: ", servidor.append(None))
> ```

`ServerProxy` es el **client stub**: cada atributo que se le pide (`servidor.add`) se convierte en una petición HTTP con el XML de la llamada. Salida:

```text
3 + 8 = 11
--> Hello World
DATA:  Probando
DATA:  Probando
Concatenar string:  ANYA
DATA:  Probando
```

Tres detalles que muestra el ejemplo:

- `add` funciona con números y con strings, porque en el servidor es un `+` de Python.
- `append` siempre retorna `DATA[0]`, el primer elemento guardado: el servidor **mantiene estado** entre llamadas. Si se vuelve a ejecutar el cliente sin reiniciar el servidor, `DATA` sigue con los valores anteriores (algo que REST evitaría).
- Llamar a una función no registrada, como `servidor.restar(1, 2)`, levanta un `xmlrpc.client.Fault` con el mensaje `method "restar" is not supported`: el error del servidor viaja de vuelta como excepción.

## RMI: invocar métodos de un objeto

Java se basa fuertemente en la programación orientada a objetos, y **RMI** (*Remote Method Invocation*) se diseñó para llevar RPC a Java. Es un tipo específico de RPC en que se invocan **métodos de un objeto**. En Python basta con registrar una instancia:

```python
from xmlrpc.server import SimpleXMLRPCServer

class RMIServer:
    def __init__(self):
        self.data = []

    def add(self, x, y):
        return x + y

    def hello_world(self):
        return "Hello World"

    def append(self, x):
        self.data.append(x)
        return self.data[0]

server = SimpleXMLRPCServer(("localhost", 4444), allow_none=True)
server.register_instance(RMIServer())
server.serve_forever()
```

El **cliente no cambia**: con `register_instance` o con `register_function`, `ServerProxy` llama igual y obtiene la misma salida. Ahora el estado vive en el atributo `self.data` del objeto.

> [!tip] Por qué el cliente no cambia
> Para el client stub solo existen nombres de operaciones y argumentos. Si detrás hay funciones sueltas o métodos de un objeto es un detalle del servidor, oculto por la transparencia de acceso.

> [!warning] `SimpleXMLRPCServer` atiende de a uno
> Procesa una petición a la vez. Para atender varios clientes en paralelo se usa `ThreadingMixIn` (como en [[05 - Sockets TCP en Python|el servidor con threads]]) o un framework distinto.

## Preguntas de repaso

> [!question]- En el ejemplo, ¿por qué `append("4444")` retorna `"Probando"`?
> Porque `f3` agrega el valor a la lista global y retorna siempre el primer elemento. Como antes se agregó `"Probando"`, ese sigue siendo `DATA[0]`.

> [!question]- ¿Qué cambia entre la versión RPC y la versión RMI del servidor, y qué cambia en el cliente?
> En el servidor, las funciones pasan a ser métodos de una clase y se registra una instancia con `register_instance`; el estado queda en el objeto. En el cliente no cambia nada.

> [!question]- ¿Qué componente cumple el rol de client stub en `xmlrpc`?
> `ServerProxy`: traduce cada llamada a un mensaje XML sobre HTTP, lo envía al servidor y convierte la respuesta (o el error) en el valor de retorno (o en una excepción `Fault`).
