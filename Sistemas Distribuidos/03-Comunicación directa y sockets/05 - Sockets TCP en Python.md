---
ramo: "Sistemas Distribuidos"
tema: "Comunicación directa y sockets"
tags:
  - sd/comunicacion
  - python
  - origen/complemento
prerrequisitos:
  - "[[02 - Paradigmas de comunicación]]"
  - "[[03 - Protocolos de transporte TCP y UDP]]"
  - "[[05 - Mecanismos de sincronización entre threads]]"
---

# Sockets TCP en Python

La comunicación directa es la forma más simple de que dos procesos se hablen: paso de mensajes, donde el emisor indica el destino del receptor con una dirección y un puerto. La herramienta clásica es el **socket**, una interfaz de entrada y salida de datos entre procesos que puede usar TCP o UDP. Sobre sockets se construye casi todo lo demás del ramo.

## Cliente y servidor

Un socket actúa como **servidor** (espera conexiones) o como **cliente** (las inicia), y cada rol sigue una secuencia de llamadas distinta:

![Llamadas de un socket TCP cliente y servidor](adjuntos/Llamadas%20de%20un%20socket%20TCP%20cliente%20y%20servidor.png)

> [!example]- Transcripción de la imagen
> - **Servidor:** `Socket()` → `Bind()` → `Listen()` → `Accept()`, que bloquea hasta que llega una conexión. Luego repite `Read()` → `Write()`.
> - **Cliente:** `Socket()` → `Connect()` (establece la conexión con el `Accept` del servidor) → `Write()` envía *data (request)* → `Read()` recibe *data (reply)*, en ciclo, y finalmente `Close()`.

## Servidor y cliente en Python

El protocolo de este ejemplo es mínimo: primero se envían **4 bytes con el largo** del mensaje y después el mensaje. Así el receptor sabe cuántos bytes leer, porque TCP entrega un flujo de bytes sin separar mensajes.

```python
# Servidor: atiende 2 clientes, uno tras otro, y devuelve el mismo mensaje (eco)
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # IPv4 + TCP
sock.bind(('localhost', 4444))
sock.listen(5)                                             # hasta 5 conexiones en espera

i = 0
while i < 2:
    connection, client_address = sock.accept()             # bloquea hasta que llegue un cliente
    largo = connection.recv(4)
    mensaje = connection.recv(int.from_bytes(largo, byteorder="big"))
    print(mensaje.decode("UTF-8"))
    connection.sendall(largo + mensaje)
    connection.close()
    i += 1
sock.close()
```

```python
# Cliente
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 4444))
mensaje = "waku waku".encode("UTF-8")
largo = len(mensaje).to_bytes(4, byteorder="big")
sock.sendall(largo)
sock.sendall(mensaje)
largo = sock.recv(4)
data = sock.recv(int.from_bytes(largo, byteorder="big"))
print(data.decode("UTF-8"))                                # waku waku
sock.close()
```

Con el servidor corriendo, dos ejecuciones del cliente imprimen `waku waku` en ambos lados y el servidor termina.

> [!warning] `recv(n)` puede entregar menos de `n` bytes
> En localhost con mensajes cortos funciona, pero en una red real un mensaje puede llegar en varios trozos. Lo robusto es leer en un ciclo hasta completar los bytes esperados (ver `recibir_exacto` abajo).

## Atender varios clientes con threads

El servidor anterior atiende **un cliente a la vez**: mientras espera los datos de uno, cualquier otro queda bloqueado. Con threads, el thread principal solo acepta conexiones y delega cada una a un thread propio:

```python
import socket, threading

def recibir_exacto(conn, n):
    datos = b""
    while len(datos) < n:                 # recv puede entregar menos bytes que n
        parte = conn.recv(n - len(datos))
        if not parte:
            raise ConnectionError("el cliente cerró la conexión")
        datos += parte
    return datos

def atender(conn, addr):
    with conn:
        largo = recibir_exacto(conn, 4)
        mensaje = recibir_exacto(conn, int.from_bytes(largo, "big"))
        conn.sendall(largo + mensaje.upper())

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(("localhost", 4445))
sock.listen()
while True:
    conn, addr = sock.accept()            # el thread principal solo acepta
    threading.Thread(target=atender, args=(conn, addr), daemon=True).start()
```

En la prueba, un cliente lento que tardaba 2 segundos en enviar su mensaje no bloqueó a uno rápido que llegó después: el rápido recibió su respuesta de inmediato.

> [!tip] Sockets + threads
> Combinar sockets con threads permite atender a muchos clientes a la vez, o incluso tener varios servidores en un mismo proceso. Es la base de un nodo que es "cliente y servidor a la vez".

La vista desde el sistema operativo (puertos, `socket()`, `bind()` y llamadas al sistema) está en [[03 - Sockets UDP y TCP: modelos y llamadas al sistema|Sockets UDP y TCP]].

## Preguntas de repaso

> [!question]- ¿Por qué el protocolo envía primero 4 bytes con el largo del mensaje?
> Porque TCP es un flujo de bytes sin límites entre mensajes. Si el receptor conoce el largo, sabe exactamente cuántos bytes forman el mensaje y dónde empieza el siguiente.

> [!question]- ¿Qué problema tiene el servidor sin threads si llega un cliente lento?
> Queda bloqueado en `recv` esperando a ese cliente, y ningún otro puede ser atendido hasta que termine, aunque esté listo.

> [!question]- ¿Qué hace `listen(5)` y qué no hace?
> Deja el socket en modo servidor con una cola de hasta 5 conexiones pendientes de `accept`. No limita a 5 los clientes atendidos en total ni crea threads.
