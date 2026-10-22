---
ramo: "Programación Avanzada"
tema: "Serialización y networking II"
tags:
  - programacion/networking
  - programacion/sockets
  - programacion/udp
  - origen/complemento
prerrequisitos:
  - "[[03 - Modelo de capas y protocolos de transporte: TCP frente a UDP]]"
  - "[[03 - Sockets TCP en Python: arquitectura y ciclo de vida]]"
---

# Sockets UDP: comunicación no orientada a conexión con datagramas

Frente a la sobrecarga y latencia del saludo de tres vías y las confirmaciones continuas de TCP, existen aplicaciones donde la velocidad extrema y la inmediatez priman sobre la entrega garantizada (por ejemplo la sincronización de posiciones en videojuegos de acción o transmisiones de telemetría en tiempo real). Para estos escenarios recurrimos a los **sockets UDP**.

## Creación y ciclo de vida de sockets UDP

Para instanciar un socket UDP en Python utilizamos el tipo **`socket.SOCK_DGRAM`** (*Datagram Socket*):

```python
import socket

sock_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
```

La diferencia arquitectónica con TCP en el código es radical: en UDP **no existe el concepto de conexión ni sesión**. Cada paquete de bytes (denominado **datagrama**) es una entidad autosuficiente enviada de forma independiente:

```
+------------------------------------+------------------------------------+
| Servidor TCP                       | Servidor UDP                       |
+------------------------------------+------------------------------------+
| 1. socket(AF_INET, SOCK_STREAM)    | 1. socket(AF_INET, SOCK_DGRAM)     |
| 2. bind((host, port))              | 2. bind((host, port))              |
| 3. listen()                        | (No existe listen)                 |
| 4. conn, addr = accept()           | (No existe accept ni nuevo socket) |
| 5. conn.recv() / conn.sendall()    | 3. data, addr = sock.recvfrom()    |
|                                    | 4. sock.sendto(data, addr)         |
+------------------------------------+------------------------------------+
```

## Implementación de Servidor UDP

El servidor solo necesita enlazar su puerto con `bind()` y comenzar a recibir datagramas de cualquier cliente mediante el método **`recvfrom()`**, que retorna tanto los datos recibidos como la dirección del remitente:

```python
import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor.bind(("127.0.0.1", 9999))
print("[Servidor UDP] Escuchando datagramas en el puerto 9999...")

# recvfrom() retorna: (bytes_recibidos, (ip_origen, puerto_origen))
mensaje, direccion_cliente = servidor.recvfrom(2048)
print(f"[Servidor UDP] De {direccion_cliente}: {mensaje.decode('utf-8')}")

# Responder directamente a la dirección de origen con sendto()
servidor.sendto("Datagrama confirmado".encode("utf-8"), direccion_cliente)
servidor.close()
```

## Implementación de Cliente UDP

El cliente no realiza ninguna llamada a `connect()`. Envía los datagramas directamente hacia el destino con el método **`sendto(datos, (host, port))`**:

```python
import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Configurar timeout para evitar congelamiento si el datagrama se pierde
cliente.settimeout(2.0)

destino = ("127.0.0.1", 9999)
cliente.sendto("Posicion: x=12, y=85".encode("utf-8"), destino)

try:
    respuesta, servidor_addr = cliente.recvfrom(2048)
    print(f"[Cliente UDP] Respuesta del servidor: {respuesta.decode('utf-8')}")
except socket.timeout:
    print("[Cliente UDP] El datagrama o la respuesta se perdió en la red.")
finally:
    cliente.close()
```

> [!warning] recvfrom() es bloqueante sin timeout
> Dado que UDP no garantiza la entrega de paquetes, si el servidor se cae o el datagrama se descarta en un router intermedio, el cliente invocando `recvfrom()` se quedará esperando para siempre. **Configura siempre un tiempo límite** mediante `cliente.settimeout(segundos)` para capturar la excepción `socket.timeout`.

> [!tip] Tamaño máximo de un datagrama UDP
> Aunque el límite teórico en IPv4 es de $65.507$ bytes, en redes reales de internet se recomienda no enviar datagramas UDP mayores a **$1.400$ bytes** para evitar que la capa IP fragmente el paquete en múltiples trozos físicos en los routers.

## Preguntas de repaso

> [!question]- ¿Por qué un servidor UDP no utiliza los métodos `listen()` ni `accept()`?
> Porque UDP no establece conexiones ni mantiene sesiones; el socket escucha directamente datagramas aislados que provienen de cualquier dirección sin negociación previa.

> [!question]- ¿Qué información adicional retorna el método `recvfrom()` en comparación con `recv()`?
> Retorna una tupla de dos elementos: los datos en bytes y la dirección de red de origen `(ip, puerto)` del equipo que emitió el datagrama.

> [!question]- ¿Qué ocurre si un paquete enviado mediante `sock.sendto()` se pierde por congestión en la red?
> El paquete se descarta de forma definitiva; el sistema operativo no notifica al emisor ni reintenta la transmisión (a menos que la aplicación implemente sus propios acuses de recibo).

> [!question]- ¿Por qué es fundamental utilizar `sock.settimeout()` al esperar respuestas con sockets UDP?
> Porque ante la pérdida de un paquete el socket quedaría bloqueado indefinidamente esperando una respuesta que nunca llegará, congelando el flujo de la aplicación.

