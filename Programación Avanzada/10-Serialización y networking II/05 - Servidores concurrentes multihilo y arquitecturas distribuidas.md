---
ramo: "Programación Avanzada"
tema: "Serialización y networking II"
tags:
  - programacion/networking
  - programacion/sockets
  - programacion/threading
  - origen/complemento
prerrequisitos:
  - "[[01 - Hilos y procesos: el módulo threading]]"
  - "[[03 - Sockets TCP en Python: arquitectura y ciclo de vida]]"
---

# Servidores concurrentes multihilo y arquitecturas distribuidas

Un servidor TCP básico que atiende peticiones en un bucle simple monofilo solo puede interactuar con un cliente a la vez. Si ese cliente mantiene la conexión abierta durante varios minutos (como en un chat en vivo o una partida multijugador), todos los demás usuarios quedarán bloqueados sin poder conectarse. Para resolverlo, combinamos sockets con programación multihilo.

## El problema del servidor secuencial monofilo

En una implementación secuencial ingenua:

```python
while True:
    conn, addr = servidor.accept()
    # Mientras atiende a este cliente, accept() no vuelve a ejecutarse
    atender_cliente_bloqueante(conn)
```

Cualquier operación lenta de entrada/salida (`recv` en espera de mensajes del usuario) congela al hilo principal, imposibilitando la atención simultánea.

## Arquitectura de Servidor Multihilo (Thread per Client)

La solución consiste en delegar cada nueva conexión a un hilo secundario independiente:

1. El **hilo principal** se encarga exclusivamente de aceptar conexiones entrantes en el socket de escucha (`accept()`).
2. En cuanto un cliente se conecta, el hilo principal crea e inicia un **hilo trabajador** pasándole el socket dedicado `conn`.
3. El hilo principal vuelve de inmediato a ejecutar `accept()`, listo para recibir al siguiente cliente sin demora.

```python
import socket
import threading

def manejar_cliente(conexion: socket.socket, direccion: tuple):
    print(f"[Servidor] Hilo iniciado para atender a {direccion}")
    try:
        while True:
            datos = conexion.recv(1024)
            if not datos:
                break  # El cliente cerró la conexión
            # Procesar y responder (servidor de eco)
            conexion.sendall(b"Recibido: " + datos)
    except ConnectionResetError:
        print(f"[Servidor] Conexión abortada por {direccion}")
    finally:
        conexion.close()
        print(f"[Servidor] Conexión cerrada con {direccion}")

def iniciar_servidor(puerto: int = 9000):
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    servidor.bind(("0.0.0.0", puerto))
    servidor.listen()
    print(f"[Servidor] Escuchando concurrentemente en el puerto {puerto}...")

    while True:
        conn, addr = servidor.accept()
        # Crear hilo daemon para atender al cliente en paralelo
        hilo = threading.Thread(target=manejar_cliente, args=(conn, addr), daemon=True)
        hilo.start()
```

## Topologías de red más allá de Cliente-Servidor

Aprender a combinar múltiples sockets permite implementar arquitecturas distribuidas complejas:

### 1. Cliente conectado a múltiples servidores
Un cliente no está limitado a hablar con un solo servidor. Puede instanciar varios sockets simultáneamente (por ejemplo conectarse a un servidor de autenticación en el puerto 8000 y a un servidor de chat en el puerto 9000), coordinando las respuestas mediante hilos o colas `queue.Queue`.

### 2. Redes entre pares (Peer-to-Peer / P2P)
En los sistemas P2P (como redes de intercambio de archivos o nodos de blockchain) desaparece la distinción rígida entre cliente y servidor. Cada nodo del sistema ejecuta simultáneamente:

- Un **socket servidor** en un puerto local para aceptar conexiones entrantes de otros pares (*peers*).
- Varios **sockets clientes** para conectarse activamente hacia otros nodos de la red.

> [!tip] Hilos daemon para conexiones de red
> Marcar los hilos de clientes como `daemon=True` permite que el servidor principal pueda detenerse limpiamente al presionar `Ctrl+C` sin quedar atascado esperando a que clientes lentos o inactivos decidan desconectarse.

## Preguntas de repaso

> [!question]- ¿Por qué un servidor monofilo no puede atender a dos clientes que mantienen su conexión abierta al mismo tiempo?
> Porque el hilo único queda bloqueado dentro de la llamada `conn.recv()` esperando datos del primer cliente, impidiéndole volver a invocar `servidor.accept()` para recibir al segundo.

> [!question]- ¿Qué rol cumple el hilo principal en un servidor multihilo frente a los hilos de trabajo?
> El hilo principal permanece en un bucle infinito dedicado únicamente a escuchar y aceptar nuevas conexiones (`accept()`), delegando la lectura y respuesta a los hilos secundarios de trabajo.

> [!question]- ¿En qué se diferencia conceptualmente una arquitectura Peer-to-Peer (P2P) del modelo Cliente-Servidor tradicional?
> En P2P no existe un nodo maestro central; cada máquina de la red opera a la vez como servidor (aceptando conexiones) y como cliente (iniciando peticiones hacia otros nodos).

> [!question]- ¿Por qué es fundamental incluir un bloque `try ... finally` al atender un socket en un hilo secundario?
> Para asegurar que el método `conexion.close()` se ejecute siempre y libere el descriptor de archivo en el sistema operativo, incluso si ocurre una excepción no controlada durante la comunicación.

