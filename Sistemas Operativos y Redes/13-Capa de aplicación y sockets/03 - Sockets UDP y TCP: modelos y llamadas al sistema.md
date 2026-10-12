---
ramo: "Sistemas Operativos y Redes"
tema: "Capa de aplicación y sockets"
tags:
  - sistemas-operativos
  - redes
  - sockets
  - udp
  - tcp
  - syscalls
  - origen/complemento
prerrequisitos:
  - "[[13-Capa de aplicación y sockets/02 - Concepto de socket e identificación por IP y puerto|02 - Concepto de socket e identificación por IP y puerto]]"
---

# Sockets UDP y TCP: modelos y llamadas al sistema

Una vez que cliente y servidor tienen un socket, pueden enviarse mensajes. Pero la secuencia de llamadas cambia según el transporte ([[12-Fundamentos de redes y modelos en capas/05 - Capas de transporte, red, enlace y física|UDP o TCP]]): con **UDP** cada mensaje viaja suelto y lleva su dirección; con **TCP** primero se establece una conexión y después los datos fluyen como por un tubo.

## La aplicación de ejemplo

El material usa un ejemplo simple: el cliente lee una línea de la entrada estándar y la envía al servidor; el servidor la convierte a mayúsculas y la devuelve; el cliente la escribe en la salida estándar.

Todo socket se crea con `int socket(int domain, int type, int protocol)`: `domain` es la familia (`AF_INET` para IPv4), `type` el tipo (`SOCK_DGRAM` para UDP, `SOCK_STREAM` para TCP) y `protocol` suele ser 0 (se deduce de los otros dos).

## UDP: sin conexión

![Diagrama de llamadas al sistema para sockets UDP no orientados a conexión](adjuntos/Diagrama%20de%20llamadas%20al%20sistema%20para%20sockets%20UDP%20no%20orientados%20a%20conexi%C3%B3n.png)

> [!example]- Transcripción de la imagen
> **Server** (*running on serverIP*): *Create socket, port=x: `serverSocket = socket(AF_INET, SOCK_DGRAM)`* → *Read UDP segment from `serverSocket`* → *Write reply to `serverSocket` specifying client address, port number*. **Client**: *Create socket: `clientSocket = socket(AF_INET, SOCK_DGRAM)`* → *Create datagram with serverIP and port=x; send datagram via `clientSocket`* → *Read datagram from `clientSocket`* → *Close `clientSocket`*.

Cada envío usa `sendto`, que recibe **el socket, un struct con el destino (IP y puerto), el buffer con los datos y flags**. El servidor tiene **un único socket común para todos los clientes**, y sabe quién envió cada mensaje gracias a la dirección (IP y puerto del cliente) que entrega `recvfrom`.

Como `recvfrom` es bloqueante, un programa que quiera enviar y recibir a la vez necesita, por ejemplo, **dos [[05-Hilos/01 - Concepto de hilo y recursos compartidos versus privados|threads]]**: uno que envía y otro que recibe.

## TCP: orientado a conexión

Antes de enviar datos hay que **establecer la conexión** con el *handshake*:

1. El servidor tiene un **socket de bienvenida** (*welcoming socket*) escuchando en un puerto conocido.
2. El cliente le pide una conexión en ese puerto (`connect`).
3. El servidor la acepta (`accept`) y **crea un socket nuevo** dedicado a ese cliente.
4. Desde ahí, el socket funciona como un **tubo** por el que el cliente envía y recibe bytes.

![Diagrama de llamadas al sistema para sockets TCP welcoming y conexión](adjuntos/Diagrama%20de%20llamadas%20al%20sistema%20para%20sockets%20TCP%20welcoming%20y%20conexi%C3%B3n.png)

> [!example]- Transcripción de la imagen
> *Client process* con su *Client socket*, y *Server process* con un *Welcoming socket* y un *Connection socket*. Una flecha *Three-way handshake* va del socket del cliente al de bienvenida; entre el socket del cliente y el de conexión hay un tubo por el que viajan *bytes* en ambas direcciones.

![Flujo de intercambio de mensajes mediante sockets UDP](adjuntos/Flujo%20de%20intercambio%20de%20mensajes%20mediante%20sockets%20UDP.png)

> [!example]- Transcripción de la imagen
> Secuencia de llamadas TCP. **Server**: `socket()`, `bind()`, `listen()`, `accept()`, `recv()`, `send()`, `close()`. **Client**: `socket()`, `connect()` (hacia `accept()`), `send()` (hacia `recv()`), `recv()` (desde `send()`), `close()`.

Con la conexión establecida se usan `send()` y `recv()` con un buffer de datos, **sin especificar la dirección**: ya está fijada por la conexión.

## UDP frente a TCP

| | UDP | TCP |
|---|---|---|
| Conexión | No (*connectionless*) | Sí (*connection oriented*): handshake |
| Sockets en el servidor | **Uno común** para todos los clientes | El de bienvenida más **uno por cada cliente**, todos en el **mismo puerto** del servidor y distinguidos por la 4-tupla (IP y puerto de origen y destino) |
| Envío | `sendto`: **cada mensaje lleva la dirección** | `send`: **sin dirección** |
| Llamadas del servidor | `socket`, `bind`, `recvfrom`, `sendto` | `socket`, `bind`, `listen`, `accept`, `recv`, `send` |

```c
/* Servidor de mayúsculas con TCP, en un solo programa (cliente y servidor locales) */
#include <arpa/inet.h>
#include <ctype.h>
#include <stdio.h>
#include <sys/socket.h>
#include <unistd.h>

int main(void) {
    int welcoming = socket(AF_INET, SOCK_STREAM, 0);           /* socket de bienvenida */
    struct sockaddr_in dir = { .sin_family = AF_INET, .sin_port = 0,
                               .sin_addr.s_addr = htonl(INADDR_LOOPBACK) };
    bind(welcoming, (struct sockaddr *)&dir, sizeof dir);
    socklen_t largo = sizeof dir;
    getsockname(welcoming, (struct sockaddr *)&dir, &largo);  /* puerto elegido por el SO */
    listen(welcoming, 5);

    int cli = socket(AF_INET, SOCK_STREAM, 0);
    connect(cli, (struct sockaddr *)&dir, sizeof dir);         /* handshake */
    int conn = accept(welcoming, NULL, NULL);                  /* socket propio de esta conexión */

    send(cli, "hola tcp", 8, 0);                               /* sin dirección: ya hay conexión */
    char buf[64] = {0};
    int n = recv(conn, buf, sizeof buf - 1, 0);
    for (int i = 0; i < n; i++) buf[i] = toupper((unsigned char)buf[i]);
    send(conn, buf, n, 0);

    char resp[64] = {0};
    recv(cli, resp, sizeof resp - 1, 0);
    printf("TCP: %s\n", resp);                                 /* HOLA TCP */
    close(cli); close(conn); close(welcoming);
    return 0;
}
```

## Preguntas de repaso

> [!question]- ¿Por qué en UDP cada envío lleva la dirección de destino y en TCP no?
> Porque UDP no establece conexión: cada datagrama es independiente y debe decir a dónde va. En TCP la conexión ya fijó los dos extremos, así que `send` no necesita dirección.

> [!question]- ¿Qué hace el socket de bienvenida en un servidor TCP?
> Escucha en un puerto conocido las solicitudes de conexión. Al aceptar una, el servidor crea un socket nuevo para ese cliente, y el de bienvenida sigue esperando a otros.

> [!question]- ¿Cuántos sockets usa un servidor UDP y uno TCP para atender a varios clientes?
> El UDP usa un único socket común para todos. El TCP usa el de bienvenida más un socket por cada conexión aceptada.

> [!question]- ¿Por qué un programa con sockets puede necesitar varios threads?
> Porque las operaciones de recepción (`recv`, `recvfrom`) son bloqueantes: mientras un thread espera datos, otro puede enviar o atender a otro cliente. Otras alternativas son crear un proceso por cliente con `fork` o vigilar varios sockets a la vez con `select`, `poll` o `epoll`.
