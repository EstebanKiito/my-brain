---
ramo: "Programación Avanzada"
tema: "Serialización y networking II"
tags:
  - programacion/networking
  - programacion/sockets
  - programacion/tcp
  - origen/complemento
prerrequisitos:
  - "[[02 - Manejo de bytes codificación y endianness]]"
  - "[[03 - Sockets TCP en Python: arquitectura y ciclo de vida]]"
---

# Transmisión de mensajes estructurados y protocolo de longitud fija

Enviar mensajes simples de texto corto por un socket TCP parece directo. Sin embargo, cuando transmitimos objetos serializados (como JSON o Pickle) o archivos de varios megabytes, surge un desafío arquitectónico mayor: TCP entrega un flujo continuo de bytes (*byte stream*) sin límites naturales entre mensajes.

## El problema del flujo continuo en TCP (Stream vs Datagram)

A diferencia de UDP, TCP **no preserva los límites de los mensajes**:

- Si un emisor ejecuta `sock.sendall(mensaje_grande)` de $10\text{ KB}$, el receptor haciendo una llamada `sock.recv(4096)` solo recibirá los primeros $4\text{ KB}$ y continuará con su ejecución creyendo erróneamente que leyó todo.
- Si un emisor realiza dos llamadas `sock.sendall(msg1)` y `sock.sendall(msg2)` muy rápido, TCP puede unirlas en un solo bloque. El receptor leerá ambos mensajes pegados y `json.loads()` arrojará error de sintaxis al no poder decodificar dos objetos juntos.

El resultado de leer sin control de longitud es la pérdida y truncamiento severo de información:

| ![Pérdida de datos](adjuntos/P%C3%A9rdida%20de%20datos%20en%20transmisi%C3%B3n%20de%20archivo%20sin%20control%20de%20chunks.png) | ![Archivo incompleto](adjuntos/Comparaci%C3%B3n%20y%20truncamiento%20de%20archivo%20recibido%20incompleto.png) |
|---|---|
| Transmisión interrumpida sin sincronización | Archivo recibido con tamaño truncado frente al original |

> [!example]- Transcripción de las imágenes
> - Falla de transmisión ingenua:
>   - La consola del receptor reporta fin prematuro de recepción antes de transferir la totalidad del archivo.
>   - La comparación en disco muestra que el archivo recibido tiene menos bytes que el emisor original.

## La solución: Protocolo de longitud prefijada (Header de 4 bytes)

Para delimitar con precisión cada mensaje, se implementa un **protocolo a nivel de aplicación**:

$$\overbrace{\text{[ 4 bytes de tamaño (Big-Endian) ]}}^{\text{Encabezado de longitud fija}} + \overbrace{\text{[ Contenido del mensaje en bytes ]}}^{\text{Cuerpo de longitud variable}}$$

1. **El emisor:** calcula cuántos bytes mide el mensaje serializado, codifica esa longitud en un entero de 4 bytes con `byteorder="big"` y envía la cabecera antes del cuerpo.
2. **El receptor:**
   - Lee exactamente los primeros 4 bytes y extrae el entero `largo_esperado`.
   - Entra en un bucle acumulando lecturas en bloques de 4096 bytes hasta completar exactamente la cantidad de bytes indicada en la cabecera.

```python
import socket

def enviar_mensaje(sock: socket.socket, contenido: bytes):
    # 1. Cabecera fija de 4 bytes indicando la longitud del cuerpo
    cabecera = len(contenido).to_bytes(4, byteorder="big")
    sock.sendall(cabecera + contenido)

def recibir_mensaje(sock: socket.socket) -> bytes:
    # 2. Leer estrictamente los 4 bytes de la cabecera
    cabecera = b""
    while len(cabecera) < 4:
        trozo = sock.recv(4 - len(cabecera))
        if not trozo:
            return b""
        cabecera += trozo
    largo_total = int.from_bytes(cabecera, byteorder="big")

    # 3. Leer en bucle acumulando chunks hasta completar el tamaño exacto
    datos = bytearray()
    while len(datos) < largo_total:
        faltante = largo_total - len(datos)
        trozo = sock.recv(min(4096, faltante))
        if not trozo:
            break
        datos.extend(trozo)
    return bytes(datos)
```

Al utilizar este protocolo por bloques (*chunks*), se garantiza la recepción íntegra sin desbordar la memoria:

| ![Transmisión robusta](adjuntos/Transmisi%C3%B3n%20robusta%20de%20archivo%20con%20protocolo%20de%20longitud%20fija.png) | ![Integridad verificada](adjuntos/Integridad%20verificada%20de%20archivo%20recibido%20con%20protocolo%20por%20chunks.png) |
|---|---|
| Recepción progresiva bloque por bloque | Archivo recibido íntegro con tamaño exacto |

> [!example]- Transcripción de las imágenes
> - Transmisión robusta:
>   - La consola muestra el progreso por bloques de 4096 bytes hasta alcanzar el tamaño exacto.
>   - La comprobación en disco ratifica que el archivo emisor y receptor son idénticos byte por byte.

> [!tip] Integración con JSON y Pickle
> Con este protocolo puedes enviar cualquier estructura: serializas con `json.dumps(obj).encode("utf-8")` o `pickle.dumps(obj)`, pasas los bytes a `enviar_mensaje()`, y en el receptor decodificas y deserializas los bytes entregados por `recibir_mensaje()`.

## Preguntas de repaso

> [!question]- ¿Por qué una sola llamada a `sock.recv(4096)` no garantiza haber recibido un mensaje completo de 3000 bytes?
> Porque TCP fragmenta y entrega los paquetes según la congestión de la red y el tamaño máximo de segmento (MTU); una llamada a `recv()` solo entrega los bytes que ya están en el búfer local en ese instante.

> [!question]- ¿Por qué se eligen exactamente 4 bytes para codificar la cabecera de longitud del mensaje?
> Porque un entero de 4 bytes (32 bits) sin signo puede representar tamaños de archivo de hasta $2^{32} - 1$ bytes ($\approx 4\text{ GB}$), suficiente para casi cualquier mensaje en memoria.

> [!question]- ¿Qué ocurre en el receptor si la cabecera indica un tamaño de 1000 bytes pero el emisor se desconecta tras enviar 500 bytes?
> La llamada `sock.recv()` retornará bytes vacíos (`b""`), permitiendo que el bucle de acumulación aborte y detecte que la conexión fue terminada prematuramente.

> [!question]- ¿Cómo resuelve el protocolo de longitud prefijada el problema de recibir dos mensajes consecutivos pegados?
> Al conocer la longitud exacta del primer mensaje, el receptor solo extrae esa cantidad de bytes del búfer, dejando el resto para que la siguiente lectura procese el segundo mensaje limpiamente.

