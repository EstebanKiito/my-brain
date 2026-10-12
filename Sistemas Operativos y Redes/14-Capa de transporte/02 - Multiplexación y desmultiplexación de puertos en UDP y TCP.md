---
ramo: "Sistemas Operativos y Redes"
tema: "Capa de transporte"
tags:
  - sistemas-operativos
  - redes
  - multiplexacion
  - desmultiplexacion
  - puertos
  - sockets
  - origen/complemento
prerrequisitos:
  - "[[14-Capa de transporte/01 - Servicios de la capa de transporte y estructura de segmentos|01 - Servicios de la capa de transporte y estructura de segmentos]]"
---

# Multiplexación y desmultiplexación de puertos en UDP y TCP

En un host corren muchos procesos que usan la red al mismo tiempo, pero todos comparten una sola conexión. **Multiplexar** es juntar los mensajes de varios procesos para enviarlos por la red; **desmultiplexar** es, al recibir, entregar cada segmento al proceso que corresponde. La pregunta clave es qué datos del segmento usa el receptor para decidirlo, y la respuesta es distinta en UDP y en TCP.

## Multiplexación: sockets y puertos

Los procesos envían sus mensajes a través de **sockets** del sistema operativo:

- cada socket se crea con un **número de puerto** específico;
- un host puede tener **múltiples sockets** (y puertos) abiertos a la vez;
- un puerto no puede estar asignado a varios sockets del mismo protocolo: si dos programas intentan usar el mismo puerto, el segundo `bind()` falla con el error "dirección en uso" (`EADDRINUSE`), salvo que se configuren opciones como `SO_REUSEADDR`.

Por ejemplo, para conectarse a una página web se abre un socket, y para hacer otra cosa se abre otro; hay que saber qué se va a hacer para saber a qué puerto conectarse.

![Asignación de puertos y sockets en hosts emisores y receptores](adjuntos/Asignaci%C3%B3n%20de%20puertos%20y%20sockets%20en%20hosts%20emisores%20y%20receptores.png)

> [!example]- Transcripción de la imagen
> Tres hosts, cada uno con su pila *Application / Transport / Network / Data link / Physical*. En el primero corre el proceso P3, en el del medio P1 y P2, y en el tercero P4. Cada proceso tiene un socket en la capa *Transport*. Las líneas azules unen P3 con P1 y P2 con P4 a través de la red: el host del medio desmultiplexa los segmentos hacia P1 o P2 según su socket.

## UDP: sin conexión

Un segmento UDP se identifica por **⟨IP destino, puerto destino⟩**. El receptor **observa el puerto de destino** y pasa el segmento al proceso asociado a ese puerto. Así, **hay un solo socket para todos los clientes**: datagramas de hosts distintos que van al mismo puerto llegan al mismo socket.

![Desmultiplexación no orientada a conexión en sockets UDP](adjuntos/Desmultiplexaci%C3%B3n%20no%20orientada%20a%20conexi%C3%B3n%20en%20sockets%20UDP.png)

> [!example]- Transcripción de la imagen
> "**Sin Conexión.** Segmento UDP identificado por: ⟨IP destino, puerto destino⟩. Receptor observa el puerto de destino. Pasa el segmento al proceso asociado al puerto de destino". El *Client process* de *Host A* envía a *Server B* un segmento con *source port: 19157, dest. port: 46428*; la respuesta vuelve con *source port: 46428, dest. port: 19157*.

El puerto de origen sirve para que el servidor sepa **a dónde responder**: en la respuesta, origen y destino se invierten.

## TCP: con conexión

La conexión se crea con el *handshake*, y desde ahí cada segmento TCP se identifica por la **4-tupla ⟨IP origen, puerto origen, IP destino, puerto destino⟩**. Por eso un servidor puede gestionar **múltiples conexiones TCP** en el mismo puerto y asociar **distintos sockets a distintos clientes**: cada socket sirve a un cliente particular.

![Desmultiplexación orientada a conexión en sockets TCP mediante 4-tupla](adjuntos/Desmultiplexaci%C3%B3n%20orientada%20a%20conexi%C3%B3n%20en%20sockets%20TCP%20mediante%204-tupla.png)

> [!example]- Transcripción de la imagen
> "**Con Conexión.** Segmento TCP identificado por: ⟨IP origen, puerto origen, IP destino, puerto destino⟩. Servidores pueden gestionar múltiples conexiones TCP. Se pueden asociar distintos sockets a distintos clientes". Tres segmentos llegan al *Web server B*, todos con *dest. port: 80* y *dest. IP: B*: dos desde el *Web client host C* (*source port* 7532 y 26145) y uno desde el *Web client host A* (*source port* 26145). El servidor los entrega a tres *Per-connection HTTP processes* distintos (*Transport-layer demultiplexing*).

```python
# Segmentos que llegan al servidor B (puerto 80), como en la figura
segmentos = [
    {"ip_o": "C", "p_o": 7532,  "ip_d": "B", "p_d": 80},
    {"ip_o": "C", "p_o": 26145, "ip_d": "B", "p_d": 80},
    {"ip_o": "A", "p_o": 26145, "ip_d": "B", "p_d": 80},
]
def socket_udp(s): return (s["ip_d"], s["p_d"])                          # 2-tupla
def socket_tcp(s): return (s["ip_o"], s["p_o"], s["ip_d"], s["p_d"])     # 4-tupla

print({socket_udp(s) for s in segmentos})   # {('B', 80)}: un solo socket
print({socket_tcp(s) for s in segmentos})   # tres sockets distintos
```

Fíjate en que dos clientes usan el mismo puerto de origen (26145), pero vienen de IP distintas (A y C): la 4-tupla los separa igual.

| | UDP | TCP |
|---|---|---|
| Identificador | ⟨IP destino, puerto destino⟩ | ⟨IP origen, puerto origen, IP destino, puerto destino⟩ |
| Sockets en el servidor | Uno para todos los clientes | Uno por cliente (por conexión) |

## Preguntas de repaso

> [!question]- ¿Con qué datos desmultiplexa un receptor UDP y uno TCP?
> UDP usa la IP y el puerto de destino. TCP usa la 4-tupla completa: IP y puerto de origen, e IP y puerto de destino.

> [!question]- ¿Por qué dos datagramas UDP de hosts distintos llegan al mismo socket?
> Porque si van al mismo puerto de destino, la IP y el puerto de destino coinciden, y UDP no mira el origen para elegir el socket.

> [!question]- ¿Cómo distingue un servidor web a dos clientes conectados al puerto 80?
> Por la 4-tupla: aunque compartan IP y puerto de destino, difieren en la IP o en el puerto de origen.

> [!question]- ¿Para qué sirve el puerto de origen en UDP si no se usa para desmultiplexar?
> Para que el receptor sepa a dónde responder: en la respuesta, ese puerto pasa a ser el de destino.
