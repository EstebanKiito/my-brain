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
prerrequisitos:
  - "[[14-Capa de transporte/01 - Servicios de la capa de transporte y estructura de segmentos|01 - Servicios de la capa de transporte y estructura de segmentos]]"
---

# Multiplexación y desmultiplexación de puertos en UDP y TCP

La multiplexación y desmultiplexación permiten que el kernel del sistema operativo comparta la infraestructura de red subyacente entre múltiples aplicaciones concurrentes. La clave reside en los identificadores de socket: mientras que UDP utiliza únicamente la dirección IP y el puerto de destino (2-tupla), TCP requiere la 4-tupla completa para diferenciar múltiples conexiones que acceden a un mismo servicio.

---

## Mecanismos de multiplexación (mis apuntes)

MULTIPLEXION
Los mensajes se envía a traves de SOCKETS
Cada socket es asociado a 1 puerto especifico
Un Host pueden tener múltiples puertos abiertos
Un Puerto NO PUEDE estar asignado a multiples sockets

![Asignación de puertos y sockets en hosts emisores y receptores](adjuntos/Asignación%20de%20puertos%20y%20sockets%20en%20hosts%20emisores%20y%20receptores.png)

> [!example]- Transcripción de la imagen
> Asignación de sockets y puertos en hosts:
> - Cada socket tiene asignado un número de puerto local único.
> - Cuando un proceso envía datos a través de su socket, el segmento incluye su puerto origen y el puerto destino del host remoto.

ej: Si quiero conectarme a una pagina http, necesito abrir un socket, si quiero hacer otro cosa, abro otro socket, tengo que saber que voy a hacer para saber el puerto a abrir

SIN CONEXION HANDSHAKE → UDP
Identificador:
- <IP-Dest, Port-Dest>
- Hay un socket que habla con un Proceso
- Hay 1 solo socket para todos los clientes

![Desmultiplexación no orientada a conexión en sockets UDP](adjuntos/Desmultiplexación%20no%20orientada%20a%20conexión%20en%20sockets%20UDP.png)

> [!example]- Transcripción de la imagen
> Desmultiplexación en UDP (sin conexión):
> - El socket UDP se identifica únicamente por `<IP destino, Puerto destino>`.
> - Datagramas provenientes de diferentes hosts (diferente IP origen o puerto origen) que coincidan en el puerto destino son entregados al mismo socket local.

CON CONEXION (HANDSHAKE) → TCP
Identificador:
- <IP-Origen, Port-Origen, IP-Dest, Port-Dest>

![Desmultiplexación orientada a conexión en sockets TCP mediante 4-tupla](adjuntos/Desmultiplexación%20orientada%20a%20conexión%20en%20sockets%20TCP%20mediante%204-tupla.png)

> [!example]- Transcripción de la imagen
> Desmultiplexación en TCP (orientado a conexión):
> - Un socket TCP establecido se identifica por la 4-tupla: `<IP origen, Puerto origen, IP destino, Puerto destino>`.
> - El host receptor utiliza los cuatro valores para dirigir el segmento al socket correspondiente. Servidores web concurrentes escuchan en el puerto 80 mediante un welcoming socket y derivan cada cliente a un socket de conexión independiente.

- En Tcp, cada socket esta asociado a un proceso
- UN SOCKET SIRVE A UN CLIENTE PARTICULAR

> [!tip] Complemento de clase: Servidores concurrentes y subprocesos/hilos
> En un servidor HTTP o base de datos que atiende miles de peticiones simultáneas en el puerto 80 o 5432, todos los clientes envían paquetes con `Puerto-Dest = 80`. El kernel utiliza la IP de origen y el puerto dinámico/efímero del cliente para desmultiplexar cada segmento entrante hacia el hilo o subproceso específico que gestiona esa sesión.

---

## Preguntas de repaso

> [!question]- ¿Por qué dos datagramas UDP con diferente dirección IP de origen llegan al mismo socket en el servidor si tienen el mismo puerto de destino?
> Porque la desmultiplexación en UDP se rige exclusivamente por la 2-tupla `(IP destino, Puerto destino)`. El socket receptor no mantiene estado de conexión individual y procesa todos los datagramas dirigidos a ese puerto local.

> [!question]- ¿Cómo distingue un servidor web TCP entre peticiones de dos clientes que se conectan simultáneamente al puerto 80?
> Utilizando la 4-tupla completa: aunque ambos paquetes tengan `Puerto-Dest = 80` y la misma `IP-Dest`, diferirán en la `IP-Origen` de cada cliente o en el `Puerto-Origen` dinámico asignado por sus sistemas operativos.

> [!question]- ¿Qué ocurre a nivel de kernel si dos aplicaciones intentan asociarse (`bind`) al mismo puerto local usando el mismo protocolo de transporte?
> La segunda llamada al sistema `bind()` fallará con el error `EADDRINUSE` (Address already in use), a menos que se configure explícitamente la opción de socket `SO_REUSEADDR` / `SO_REUSEPORT` bajo condiciones admitidas por el sistema operativo.

