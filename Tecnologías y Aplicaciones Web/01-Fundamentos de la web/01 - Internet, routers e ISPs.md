---
ramo: "Tecnologías y Aplicaciones Web"
tema: "Fundamentos de la web"
tags:
  - web
  - internet
  - redes
  - origen/complemento
prerrequisitos: []
---

# Internet, routers e ISPs

Antes de escribir una aplicación web conviene saber qué hay entre el navegador y el servidor. **Internet** es la infraestructura técnica que permite que los computadores se comuniquen: una red de redes interconectadas. **La web** es solo uno de los servicios que funcionan sobre ella (también existen el correo, los juegos en línea o las videollamadas). Esta nota recorre esa infraestructura física desde el computador del usuario hasta el otro lado del mundo.

## Brevísima historia

| Año | Hito |
|---|---|
| 1969 | ARPANET, la primera red de computadores |
| 1971 | Primer email, dentro de ARPANET |
| 1989 | Tim Berners-Lee inventa la WWW y HTTP |
| 1989-1991 | Primera versión de HTML |
| 1995 | Brendan Eich crea JavaScript |
| 1995-2001 | Primera guerra de navegadores (Netscape contra Internet Explorer) |
| 2004-2017 | Segunda guerra de navegadores (Firefox y luego Chrome) |

## De dos computadores a una red mundial

Dos computadores se pueden conectar de forma **física** (cable Ethernet) o **inalámbrica** (Wi-Fi, Bluetooth). El problema aparece al escalar: para que $N$ computadores se hablen todos con todos se necesitan $\frac{N(N-1)}{2}$ conexiones uno a uno, lo que es inviable.

La solución es un computador especial, el **router**, cuyo único trabajo es asegurar que un mensaje enviado de A a B llegue a B y no a otro. Con un router cada máquina necesita **una sola** conexión (la suya al router). Como el router es solo otro computador, se pueden conectar routers entre sí y formar redes cada vez más grandes.

Para salir de la red local hace falta un **módem**, que traduce la señal de la red a la que viaja por la infraestructura telefónica o de fibra, y un **ISP** (*Internet Service Provider*): una compañía que maneja "routers especiales" conectados entre sí y con los de otros ISPs.

![Redes domésticas conectadas mediante ISPs](adjuntos/Redes%20dom%C3%A9sticas%20conectadas%20mediante%20ISPs.png)

> [!example]- Transcripción de la imagen
> - A la izquierda, cinco computadores (A a E) conectados a un mismo router; el router se conecta a un módem y el módem al **ISP 1**.
> - A la derecha, la misma estructura reflejada: A' a E', su router, su módem y el **ISP 2**.
> - Entre ISP 1 e ISP 2 hay una conexión troncal gruesa, con ramificaciones hacia otros ISPs.
> - Recorrido de un mensaje: usuario → router → módem → ISP → cables → ISP → módem → router → destino.

> [!tip] Router frente a módem
> El **router** crea la red local (celular, TV y PC de una casa). El **módem** conecta esa red local a Internet, es decir, al ISP. A veces vienen en una misma caja, pero cumplen funciones distintas.

## Qué aporta un ISP

Sin un ISP, cada usuario tendría que costear sus propios cables y negociar conexiones con otros proveedores y centros de datos. El ISP acerca toda esa infraestructura a los clientes finales. Los ISPs se encuentran en los **IXP** (*Internet exchange point*, o punto neutro): lugares físicos donde distintos operadores intercambian tráfico. En Chile existe PIT Chile, un IXP distribuido en varios datacenters.

Entre continentes el tráfico viaja por **cables submarinos** de fibra óptica (como Humboldt o Curie, que llega a Valparaíso). Cada cable termina en una **cable landing station**, desde donde se interconecta con datacenters, IXPs e ISPs. La aplicación Submarine Cable Map permite explorarlos.

## Redes según su alcance

- **LAN** (*local area network*): conexión local entre dispositivos, como el Wi-Fi de una casa, donde todos salen a Internet por el mismo router.
- **MAN** (*metropolitan area network*): une varias LAN cercanas geográficamente.
- **WAN** (*wide area network*): una red mucho más amplia; el propio Internet es una WAN.

Al compartir internet desde un celular (*tethering*), el teléfono cumple el papel de un router doméstico para los dispositivos conectados a él.

> [!warning] Internet no es la web
> Internet es la infraestructura (cables, routers, protocolos). La web es un sistema de documentos y aplicaciones que se accede con un navegador y que usa esa infraestructura mediante HTTP.

La misma arquitectura vista desde la teoría de redes está en [[01 - Arquitectura de Internet, nodos, enlaces y protocolos|Arquitectura de Internet]].

## Preguntas de repaso

> [!question]- ¿Por qué un router reduce drásticamente la cantidad de conexiones necesarias?
> Sin router, $N$ computadores necesitan $\frac{N(N-1)}{2}$ enlaces para hablarse todos con todos. Con un router, cada uno necesita uno solo (hacia el router), que se encarga de reenviar cada mensaje a su destino.

> [!question]- ¿Qué diferencia hay entre el router y el módem de una casa?
> El router arma la red local y reparte los mensajes entre los dispositivos de la casa; el módem conecta esa red local con la red del ISP, traduciendo la señal al medio físico del proveedor.

> [!question]- ¿Para qué existen los IXP si cada ISP ya tiene sus propios routers?
> Porque los ISPs necesitan intercambiar tráfico entre sí para que un cliente de uno llegue al servidor alojado en otro. El IXP es el punto físico común donde lo hacen, sin dar la vuelta por redes de terceros.
