---
ramo: "Programación Avanzada"
tema: "Serialización y networking II"
tags:
  - programacion/networking
  - programacion/sockets
  - programacion/tcp
  - origen/complemento
prerrequisitos:
  - "[[02 - Fundamentos de redes: arquitectura cliente-servidor, sockets y puertos]]"
  - "[[03 - Modelo de capas y protocolos de transporte: TCP frente a UDP]]"
  - "[[02 - Manejo de bytes codificación y endianness]]"
---

# Sockets TCP en Python: arquitectura y ciclo de vida

Mientras que librerías de alto nivel como `requests` o `Flask` abstraen los detalles de la red bajo peticiones HTTP, muchos sistemas (como servidores de videojuegos, servicios de chat o protocolos industriales) necesitan comunicarse directamente sobre conexiones **TCP puras**. En Python, esta interacción de bajo nivel se implementa mediante el módulo nativo **`socket`**.

## ¿Qué es un Socket de bajo nivel?

Un socket es una abstracción del sistema operativo que representa el punto final (*endpoint*) de una conexión de red bidireccional. Permite a un programa leer y escribir datos a través de la red como si se tratara de un archivo local.

![Analogía de socket](adjuntos/Analog%C3%ADa%20f%C3%ADsica%20de%20conexi%C3%B3n%20de%20un%20socket%20de%20red.jpg)

> [!example]- Transcripción de la imagen
> - Analogía física de socket:
>   - Un enchufe y conector eléctrico como metáfora del acoplamiento físico entre dos extremos que establecen un canal continuo de energía o datos.

Para crear un socket TCP en Python especificamos la familia de direcciones y el tipo de protocolo:

```python
import socket

# AF_INET = Protocolo IPv4 | SOCK_STREAM = Protocolo orientado a flujo TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

## Ciclo de vida y métodos de un Servidor TCP

El servidor cumple un rol pasivo y sigue un flujo estricto de cuatro pasos:

1. **`bind((host, port))`:** vincula el socket a una dirección IP y puerto local. Usar `host="127.0.0.1"` restringe las conexiones a la misma máquina; usar `host=""` o `"0.0.0.0"` permite conexiones desde cualquier red externa.
2. **`listen()`:** activa el socket en modo de escucha para aceptar clientes entrantes.
3. **`conn, addr = accept()`:** llamada bloqueante que espera la llegada de un cliente. Cuando este se conecta, **retorna dos valores cruciales**:
   - `conn`: un **nuevo socket independiente** creado por el sistema operativo exclusivamente para conversar con ese cliente específico.
   - `addr`: tupla con la IP y puerto efímero del cliente `(ip, puerto)`.
   - *El socket original del servidor continúa libre para seguir escuchando a nuevos clientes.*
4. **`conn.recv(buffer_size)` y `conn.sendall(data)`:** intercambian bytes por el canal establecido. Si `recv()` retorna `b""` (cadena de bytes vacía), indica que el cliente cerró la conexión.

```python
import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Opción para liberar el puerto inmediatamente al reiniciar el servidor
servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

servidor.bind(("127.0.0.1", 8000))
servidor.listen()
print("[Servidor] Esperando cliente en el puerto 8000...")

conexion_cliente, direccion = servidor.accept()
print(f"[Servidor] Conectado con {direccion}")

datos = conexion_cliente.recv(1024)
print(f"[Servidor] Mensaje recibido: {datos.decode('utf-8')}")

conexion_cliente.sendall("Mensaje recibido con éxito".encode("utf-8"))
conexion_cliente.close()
servidor.close()
```

## Ciclo de vida de un Cliente TCP

El cliente es simple y directo:

```python
import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(("127.0.0.1", 8000))  # Inicia el handshake TCP

# Transmitir bytes
cliente.sendall("Hola servidor".encode("utf-8"))

# Recibir respuesta del servidor
respuesta = cliente.recv(1024)
print(f"[Cliente] Respuesta: {respuesta.decode('utf-8')}")

cliente.close()
```

> [!warning] send() vs sendall(): la trampa del envío parcial
> Nunca utilices `sock.send(datos)` en producción. Si el búfer de red del sistema operativo está saturado, `send()` puede transmitir solo una fracción de los bytes y retornar el número enviado, dejando datos truncados. En su lugar, usa siempre **`sock.sendall(datos)`**, que reintenta en un bucle continuo hasta garantizar la salida total del mensaje.

> [!tip] Liberar puertos con SO_REUSEADDR
> Tras cerrar un servidor, el sistema operativo mantiene el puerto bloqueado durante unos minutos en estado `TIME_WAIT`. Activar `servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)` antes del `bind()` evita el molesto error `Address already in use` al reiniciar.

## Preguntas de repaso

> [!question]- ¿Qué representan los dos valores que retorna la función `servidor.accept()`?
> Retorna un nuevo objeto `socket` dedicado exclusivamente a intercambiar datos con ese cliente, y una tupla `(ip, puerto)` con la dirección de origen del cliente conectado.

> [!question]- ¿Cómo detecta un servidor que el cliente ha cerrado la conexión TCP en una llamada a `recv()`?
> Cuando la llamada `conn.recv(buffer_size)` retorna una secuencia de bytes completamente vacía (`b""`), indicando el fin de la transmisión (*EOF*).

> [!question]- ¿Por qué es una mala práctica utilizar `sock.send()` en lugar de `sock.sendall()`?
> Porque `send()` no garantiza enviar todos los datos entregados si el búfer de red está ocupado, obligando al programador a gestionar bucles manuales de reintento para evitar datos truncados.

> [!question]- ¿Para qué sirve configurar la opción `SO_REUSEADDR` en el socket del servidor?
> Permite volver a enlazar (*bind*) el mismo puerto de red inmediatamente después de detener el programa, sorteando el tiempo de espera de seguridad del sistema operativo.

