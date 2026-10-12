---
ramo: "Sistemas Operativos y Redes"
tema: "Capa de aplicación y sockets"
tags:
  - sistemas-operativos
  - redes
  - sockets
  - puertos
  - direccionamiento
  - origen/complemento
prerrequisitos:
  - "[[13-Capa de aplicación y sockets/01 - Arquitecturas de aplicación y modelos de comunicación|01 - Arquitecturas de aplicación y modelos de comunicación]]"
---

# Concepto de socket e identificación por IP y puerto

¿Cómo logra un proceso comunicarse por la red? A través de un **socket**: el elemento de software que el SO le da a un proceso para enviar y recibir por la red, igual que un descriptor de archivo le sirve para leer y escribir un archivo.

## Qué es un socket

- Es una **puerta de entrada y salida** del sistema hacia la red.
- **Utiliza los servicios de la capa de transporte** (la capa inferior): [[12-Fundamentos de redes y modelos en capas/05 - Capas de transporte, red, enlace y física|TCP o UDP]].
- Es una **interfaz entre el programador y la red**: el programador elige el **tipo de servicio** (TCP o UDP) y la **dirección del host remoto** (IP + puerto).
- Solo existe en los hosts de origen y destino, no en los routers.

![Concepto de socket e identificación por dirección IP y puerto](adjuntos/Concepto%20de%20socket%20e%20identificaci%C3%B3n%20por%20direcci%C3%B3n%20IP%20y%20puerto.png)

> [!example]- Transcripción de la imagen
> "**Socket:** elemento de software que interactúa con la red". *Computer 1* y *Computer 2*, cada uno con un *Process* conectado a un *Socket Address* (`110.120.30.40.71`); ambos sockets se unen a través de la nube *Computer Network*. Texto: "Socket es una puerta de entrada/salida al sistema. Socket utiliza servicios de transporte (capa inferior). Socket **es una interfaz** para entre el programador y la red. Programador puede controlar parámetros del socket: tipo de servicio de transporte (TCP / UDP); direccionamiento del host remoto (IP + puerto)".

## IP + puerto: a quién va el mensaje

Para que un mensaje llegue al proceso correcto hacen falta dos datos:

- la **dirección IP**, que identifica el **dispositivo**;
- el **puerto**, que identifica el **proceso** dentro de ese dispositivo.

La IP sola no basta: en un mismo computador corren muchos programas de red a la vez, y el puerto dice a cuál de ellos va el mensaje.

| Servicio | Puerto por defecto |
|---|---|
| HTTP | 80 |
| HTTPS | 443 |
| SSH | 22 |
| DNS | 53 |

Por eso [https://www.google.com:443](http://www.google.com:443) carga la misma página que `https://www.google.com`: 443 es el puerto que HTTPS usa por defecto. Con otro número, lo más probable es que no haya ningún servidor web escuchando ahí.

Los puertos son números de 16 bits (0 a 65535):

| Rango | Uso |
|---|---|
| 0 – 1023 | **Bien conocidos**: servicios estándar (también FTP 20/21 y SMTP 25); usarlos suele requerir privilegios de administrador |
| 1024 – 49151 | **Registrados** ante la IANA para aplicaciones específicas |
| 49152 – 65535 | **Dinámicos o efímeros**: el SO los asigna temporalmente a los clientes |

## TCP o UDP: qué necesita el servicio

| | TCP | UDP |
|---|---|---|
| Comunicación | **Confiable**, más lenta | **Rápida**, no confiable: no asegura que llegue todo |
| Conviene para | Archivos, correos, documentos web: **no perder datos** | Streaming, telefonía: **velocidad** |

## Ejemplo: dos procesos conversando

```python
import socket, threading

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # TCP
servidor.bind(("127.0.0.1", 0))         # puerto 0: el SO elige uno libre
servidor.listen()
ip, puerto = servidor.getsockname()
print("servidor escuchando en", (ip, puerto))

def atender():
    conn, cliente = servidor.accept()
    print("conexión 4-tupla:", cliente, "->", conn.getsockname())
    conn.sendall(b"hola " + conn.recv(100))
    conn.close()

hilo = threading.Thread(target=atender); hilo.start()
with socket.create_connection((ip, puerto)) as c:                  # el cliente usa un puerto efímero
    c.sendall(b"mundo")
    print("respuesta:", c.recv(100).decode())
hilo.join(); servidor.close()
```

Al ejecutarlo, el servidor escucha en un puerto que elige el SO, y el cliente se conecta desde otro puerto, también asignado por el SO. Una conexión TCP queda identificada por la **4-tupla** (IP origen, puerto origen, IP destino, puerto destino). Por eso un servidor puede atender muchas conexiones en el mismo puerto: cada cliente aporta una IP o un puerto de origen distintos. Un socket UDP, en cambio, se identifica solo por (IP destino, puerto destino): todos los datagramas que llegan a ese puerto van al mismo socket.

## Preguntas de repaso

> [!question]- ¿Qué es un socket?
> El elemento de software con que un proceso se comunica por la red: una puerta de entrada y salida que usa los servicios de TCP o UDP y donde el programador define el tipo de transporte y la dirección remota (IP + puerto).

> [!question]- ¿Por qué no basta la IP para entregar un mensaje?
> Porque la IP identifica el dispositivo, pero en él corren muchos procesos. El puerto indica a cuál proceso va el mensaje.

> [!question]- ¿Cuándo conviene TCP y cuándo UDP?
> TCP cuando no se puede perder información (archivos, correo, páginas web). UDP cuando importa más la velocidad que perder algún dato (streaming, telefonía).

> [!question]- ¿Por qué `https://www.google.com:443` muestra la misma página?
> Porque 443 es el puerto por defecto de HTTPS: escribirlo explícitamente no cambia nada.
