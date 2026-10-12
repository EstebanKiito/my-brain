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
prerrequisitos:
  - "[[13-Capa de aplicación y sockets/02 - Concepto de socket e identificación por IP y puerto|02 - Concepto de socket e identificación por IP y puerto]]"
---

# Sockets UDP y TCP: modelos y llamadas al sistema

La programación de aplicaciones de red se estructura sobre dos paradigmas fundamentales de transporte: datagramas sin conexión ([[12-Fundamentos de redes y modelos en capas/05 - Capas de transporte, red, enlace y física|UDP]]) y flujo continuo orientado a conexión ([[12-Fundamentos de redes y modelos en capas/05 - Capas de transporte, red, enlace y física|TCP]]). Cada modelo exige secuencias distintas de llamadas al sistema (`socket`, `bind`, `listen`, `accept`, `connect`, `sendto`, `recvfrom`).

---

## Modelos de conexión y llamadas al sistema (mis apuntes)

APLICACION CON SOCKETS (ejemplo)
- Cliente lee una línea desde la entrada estándar (stdin)
- Cliente envía línea al servidor
- Servidor recibe línea
- Servidor convierte caracteres a mayúsculas (uppercase)
- Servidor envía línea modificada al cliente2
- Cliente2 recibe línea
- Cliente2 escribe la línea en la salida estándar (stdout)

![Flujo de intercambio de mensajes mediante sockets UDP](adjuntos/Flujo%20de%20intercambio%20de%20mensajes%20mediante%20sockets%20UDP.png)

> [!example]- Transcripción de la imagen
> Flujo cliente-servidor mediante sockets UDP: el cliente crea un socket, empaqueta el mensaje junto con la dirección de destino (IP y puerto) en un datagrama y lo envía con `sendto`. El servidor lee el datagrama con `recvfrom`, procesa la solicitud y responde enviando un datagrama de vuelta a la dirección origen extraída del paquete recibido.

Conexión UDP

![Diagrama de llamadas al sistema para sockets UDP no orientados a conexión](adjuntos/Diagrama%20de%20llamadas%20al%20sistema%20para%20sockets%20UDP%20no%20orientados%20a%20conexión.png)

> [!example]- Transcripción de la imagen
> Diagrama de llamadas para sockets UDP:
> - Servidor: `socket()` $\to$ `bind()` $\to$ `recvfrom()` (bloqueante) $\to$ procesa $\to$ `sendto()`.
> - Cliente: `socket()` $\to$ `sendto()` $\to$ `recvfrom()` $\to$ `close()`. No existe fase de `listen` ni `accept`.

En Resumen: Existe un envio de mensaje, donde se entrega
- el socket,
- struct con datos destino →(Ip destino y puerto),
- buffer con los datos,
- flags

Socket UDP
Si hosteo un servidor con un socket UDP
Tendre un socket comun abierto para todos los clientes → Esperando la enviada de informacion
- CONECTION LESS
- Unico socket para clientes
- Identificador clietnes (IPcliente, PuertoCliente) → Se de donde viene la informacion
- + (IPsrc, Portsrc, IPdestinto, Portdestino) → Saber a donde mandarlos
de sist Op: Para enviar y recibir informacion necesitaria 2 Threads (porque son bloqueantes), uno para enviar y otro para recibir}

Conexion TCP
Requiere un proceso anterior → ESTABLECER CONEXION : HANDSHAKE
Existe un socket Welcoming, el cliente le habla para pedirle conexion, acuerdan la tasa de transferencia de datos y otras cosas, y luego de esto, le entrega un socket especifico para ti
Con esto el socket se transforma en un tubo, por donde el clinete le manda datos y recibe

![Diagrama de llamadas al sistema para sockets TCP welcoming y conexión](adjuntos/Diagrama%20de%20llamadas%20al%20sistema%20para%20sockets%20TCP%20welcoming%20y%20conexión.png)

> [!example]- Transcripción de la imagen
> Diagrama de llamadas para sockets TCP:
> - Servidor: `socket()` $\to$ `bind()` al puerto welcoming $\to$ `listen()` $\to$ `accept()` (bloquea hasta que llega cliente; crea nuevo socket de conexión) $\to$ `read()` / `recv()` $\to$ `write()` / `send()` $\to$ `close()`.
> - Cliente: `socket()` $\to$ `connect()` (inicia 3-way handshake con welcoming socket) $\to$ `write()` / `send()` $\to$ `read()` / `recv()` $\to$ `close()`.

Una vez que se establece la conexion , los procesos pueden enviarse datos usando
SEND() Y RECV()
Enviar un mensaje atraves de un socket, tiene un buffer de datos a enviar
- NO NECESITA ESPECIFICAR DIRECCION! → Dado que ya esta establecida la conexión
Pregunta de prueba: Diferencia entre socket tcp y udp, el tcp no envia la direccion y udp siempre

Socket TCP
- CONECTION ORIENTED → TCP HANDSHAKE
- Por cada cliente → Un puerto (cada cliente va a ser escuchado por un socket en un servidor)

Pasos de conexion
Establecimiento de conexión: TCP Handshake (saludo de manos)
- Requiere establecer conexión antes de enviar
- Cliente inicia solicitud de conexión en un puerto conocido del servidor
- Servidor debe tener un socket en ese puerto
- Servidor debe aceptar la conexión
- Al aceptar la conexión, servidor asigna nuevo socket para la conexión

Al nivel de C, ambos (cliente/servidor) inicializan un Socket, el servidor tendria que aceptar la conexión (TCP: HANDSHAKE)

En resumen (pregunta de prueba)
UDP: Conexion común (un puerto para todos)
TCP: Conexion única (un puerto por cada conexion)

> [!warning] Posible error en apuntes: Sockets vs Puertos en servidores TCP
> En los apuntes se menciona "Por cada cliente un puerto" y "TCP: Conexion única (un puerto por cada conexion)". En realidad, el servidor sigue utilizando el **mismo puerto local** (por ejemplo, el puerto 80) para todos los clientes concurrentes. Lo que se crea por cada cliente es un nuevo **descriptor de socket** (socket de conexión devuelto por `accept`), diferenciado por la 4-tupla `(IP_orig, Puerto_orig, IP_dest, Puerto_dest)`.

---

## Preguntas de repaso

> [!question]- ¿Por qué `sendto()` en UDP requiere la estructura de dirección de destino pero `send()` en TCP no?
> Porque UDP es sin conexión (*connectionless*) y cada datagrama se envía de forma independiente hacia un destinatario explícito. En cambio, en TCP la conexión ya fue establecida previamente mediante el handshake (`connect` / `accept`), fijando de antemano el par emisor-receptor.

> [!question]- ¿Qué rol cumple el *welcoming socket* en un servidor TCP?
> Es el socket pasivo creado con `socket()`, asociado a un puerto con `bind()` y puesto a la escucha con `listen()`. Su única función es esperar y aceptar nuevas solicitudes de conexión entrantes (`accept`), delegando la transferencia real de datos a un socket nuevo de conexión individual.

> [!question]- ¿Por qué las operaciones de socket por defecto son bloqueantes y cómo se atienden múltiples clientes concurrentes?
> Porque `recv()` o `recvfrom()` suspenden la ejecución del proceso/hilo en el kernel hasta que lleguen datos al buffer de recepción. Para atender múltiples clientes concurrentemente se utilizan arquitecturas multihilo ([[05-Hilos/01 - Concepto de hilo y recursos compartidos versus privados|hilos de atención]]), múltiples procesos hijos (`fork`) o multiplexación no bloqueante de E/S (`select`/`poll`/`epoll`).

