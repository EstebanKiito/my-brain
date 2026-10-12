---
ramo: "Sistemas Operativos y Redes"
tema: "Fundamentos de redes y modelos en capas"
tags:
  - redes/fundamentos
  - redes/arquitectura
  - origen/complemento
prerrequisitos:
  - "[[Sistemas Operativos y Redes/01-Estructura de sistemas operativos/01 - Qué es un sistema operativo\|01 - Qué es un sistema operativo]]"
---

# Arquitectura de Internet, nodos, enlaces y protocolos

¿Para qué sirven las redes de datos? Para que **un proceso se comunique con otro**. Si el otro proceso está en la misma máquina, basta con un pipe o memoria compartida. Si está en otra, aparecen preguntas nuevas: dónde está el otro proceso, por qué medio se envía (¿cable?, ¿aire?), cómo se expresa el mensaje en ese medio, si se manda completo, a quién se le transmite, cómo se encamina hasta el destinatario y si este está dispuesto a recibirlo. Las redes responden esas preguntas.

## Internet: una red de redes

La red más grande es **Internet**, una **interconexión de redes más pequeñas**, cada una con su propia estructura: redes domésticas, empresariales, móviles y las de los proveedores.

![Estructura general de interconexión de redes e Internet](adjuntos/Estructura%20general%20de%20interconexi%C3%B3n%20de%20redes%20e%20Internet.png)

> [!example]- Transcripción de la imagen
> Varias nubes de redes conectadas: una **Mobile Network** (teléfonos, notebook, auto y una antena celular), dos **Home Network** (computadores, router y módem conectados por cables de poste), un **Local or Regional ISP** y un **National or Global ISP** (mallas de routers) y una **Enterprise Network** (computadores, switches, puntos de acceso inalámbricos y servidores).

## Los elementos de una red

| Elemento | Qué es | Ejemplos |
|---|---|---|
| **Nodos** (*hosts*) | Dispositivos de **origen y destino** de los mensajes | Computador, celular, servidor |
| **Enlaces** | Por donde se **transmiten** los datos; cada uno varía en velocidad y calidad | Cable, fibra óptica, wifi, datos móviles |
| **Dispositivos de intercambio** | Deciden por dónde **encaminar** el mensaje para que llegue a su destino | **Routers**, **switches** |
| **Puntos de acceso** | Conectan los dispositivos a la red | Módem, *access point* (inalámbrico), antena celular |
| **Proveedores de acceso** | Empresas que venden el servicio de conexión | ISP (*Internet Service Provider*) |

- El **switch** comparte la conexión entre varios dispositivos de una red local, como una zapatilla eléctrica comparte un enchufe.
- El **router** conecta redes distintas y decide hacia dónde enviar cada paquete; en una casa, conecta la red local con la del ISP.
- El **módem** (*MOdulador-DEModulador*) transforma la señal: convierte la señal digital de los equipos en una señal adecuada para el medio físico del proveedor (por ejemplo, analógica por cable) y hace la transformación inversa con lo que llega.

## Cómo se transmite: paquetes y protocolos

La información **no se transmite byte a byte ni completa**: se divide en unidades llamadas **paquetes**. Internet es una **red de paquetes**: los routers reenvían cada paquete hacia su destino, y los paquetes de un mismo mensaje pueden ir por caminos distintos y llegar en distinto orden.

Las **reglas para intercambiar paquetes** son los **protocolos**. Dos son críticos:

- **IP** (*Internet Protocol*): lleva cada paquete de una dirección a otra.
- **TCP** (*Transmission Control Protocol*; el material lo nombra *Transport Control Protocol*): busca la **integridad del mensaje**, que lo enviado llegue completo, correcto y en orden aunque haya viajado en pedazos por caminos distintos.

Para que todos sigan el mismo protocolo se acuerdan **estándares**, no implementaciones: los define la **IETF** (*Internet Engineering Task Force*) y se publican como **RFC** (*Request For Comments*).

## Un ejemplo: de la casa al servidor

![Comunicación entre procesos clientes y servidores en la red](adjuntos/Comunicaci%C3%B3n%20entre%20procesos%20clientes%20y%20servidores%20en%20la%20red.png)

> [!example]- Transcripción de la imagen
> Flechas rojas a mano muestran el recorrido de un paquete: sale de un computador de la **Home Network** con dirección **192.168.1.10**, pasa por el router y el módem de la casa (dirección **180.106.50.27**), cruza el **Local or Regional ISP** y entra a la **Enterprise Network** hasta un servidor con dirección **146.155.13.75**.

Un servidor con IP `146.155.13.75` tiene un proceso **escuchando**, esperando que le llegue algo. Desde la casa se le envía un paquete a través de los routers. `192.168.1.10` es la dirección **local** del computador dentro del hogar, y `180.106.50.27` es la dirección **pública** con que la casa se identifica hacia afuera. Las direcciones como `192.168.x.x` son privadas (RFC 1918), y el router las traduce a la pública mediante [[04 - Configuración dinámica con DHCP y traducción de direcciones NAT|NAT]]. Los procesos usan una **API** de red para interactuar con procesos en otra parte de la red, sin preocuparse de este recorrido.

> [!tip] Un protocolo es como una conversación
> Entre personas: "Hola" → "Hola" → "¿Tienes la hora?" → "Las 2:00". Entre computadores: *TCP connection request* → *TCP connection reply* → `GET http://awl.com/kurose-ross` → *archivo*. En ambos casos hay un formato de mensajes (**sintaxis**), un significado (**semántica**) y un orden con la acción esperada ante cada mensaje (**temporización**): eso es lo que define un protocolo.

## Preguntas de repaso

> [!question]- ¿Qué son los nodos, los enlaces y los dispositivos de intercambio?
> Los nodos (hosts) son el origen y el destino de los mensajes; los enlaces son los medios por donde viajan los datos; los dispositivos de intercambio (routers y switches) deciden por dónde encaminar cada mensaje.

> [!question]- ¿Qué diferencia hay entre un switch y un router?
> El switch comparte la conexión entre los dispositivos de una misma red local. El router conecta redes distintas y decide hacia dónde reenviar cada paquete.

> [!question]- ¿Qué hace un módem?
> Transforma la señal digital de los equipos en la señal que usa el medio físico del proveedor (modula) y hace la conversión inversa con la señal que llega (demodula).

> [!question]- ¿Por qué se necesitan TCP además de IP?
> Porque IP lleva paquetes sueltos de un punto a otro, pero estos pueden perderse, desordenarse o tomar caminos distintos. TCP asegura que el mensaje llegue completo, correcto y en orden.
