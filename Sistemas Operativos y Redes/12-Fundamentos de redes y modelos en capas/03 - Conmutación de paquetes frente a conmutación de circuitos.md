---
ramo: "Sistemas Operativos y Redes"
tema: "Fundamentos de redes y modelos en capas"
tags:
  - redes/nucleo
  - redes/conmutacion
  - origen/complemento
prerrequisitos:
  - "[[Sistemas Operativos y Redes/12-Fundamentos de redes y modelos en capas/01 - Arquitectura de Internet, nodos, enlaces y protocolos|01 - Arquitectura de Internet, nodos, enlaces y protocolos]]"
---

# Conmutación de paquetes frente a conmutación de circuitos

Una vez que los datos entran a la red, ¿cómo cruzan el núcleo hasta el destino? Hay dos enfoques opuestos. Internet usa la **conmutación de paquetes**: cada paquete viaja por su cuenta y los routers deciden hacia dónde reenviarlo. La red telefónica tradicional usa la **conmutación de circuitos**: antes de hablar, se reserva un camino completo de extremo a extremo.

## La demora de transmisión

Transmitir $L$ bits sobre un enlace que soporta $R$ bits por segundo demora:

$$d_{\text{trans}} = \frac{L}{R}$$

Por ejemplo, un paquete de 1500 bytes ($L = 12\,000$ bits) en un enlace de 100 Mbps tarda $12\,000 / 10^8 = 120\ \mu s$.

## Conmutación de paquetes (*packet switching*)

Internet es una **red de paquetes**: cada paquete lleva etiquetas de origen y destino, y la infraestructura lo mira, lo examina y lo reenvía. Cada router:

1. **Almacena** el paquete completo (*store*);
2. **Examina** el paquete y determina el punto de reenvío (*forward*);
3. Usa **tablas de reenvío** (*forwarding tables*), un mapeo del tipo "todos los paquetes cuyo destino empiece con `120.…`, mándalos por este camino".

![Conmutación de paquetes packet switching y tablas de reenvío](adjuntos/Conmutaci%C3%B3n%20de%20paquetes%20packet%20switching%20y%20tablas%20de%20reenv%C3%ADo.png)

> [!example]- Transcripción de la imagen
> Un *Source* envía los paquetes 1, 2 y 3 por un enlace de *R bps* hacia un router: "Front of packet 1 stored in router, awaiting remaining bits before forwarding". Del router sale un enlace hacia el *Destination*.

Como cada router espera el paquete completo antes de reenviarlo, si la ruta tiene $N$ enlaces iguales:

$$d_{\text{end-to-end}} = N \times \frac{L}{R}$$

La **tasa** queda determinada por **el enlace más lento**, y el router puede sufrir **congestión**: su memoria es limitada. Si llegan más paquetes de los que puede enviar, se forma una **cola**, y si la cola se llena, se pierden paquetes. Con más routers y rutas alternativas es más fácil manejar la congestión, porque el tráfico se puede desviar.

![Colas de espera en routers y pérdida de paquetes por congestión](adjuntos/Colas%20de%20espera%20en%20routers%20y%20p%C3%A9rdida%20de%20paquetes%20por%20congesti%C3%B3n.png)

> [!example]- Transcripción de la imagen
> "Tasa de transmisión determinada por el enlace más lento. *Router* puede sufrir **congestión**. Si hay $N$ enlaces iguales en la ruta, el tiempo de transmisión de origen a destino (*end-to-end delay*) es: $d_{end-to-end} = N \times \frac{L}{R}$". En el diagrama, A y B envían por enlaces de *10 Mbps Ethernet* a un router cuyo enlace de salida es de *1.5 Mbps*; se forma una *Queue of packets waiting for output link* hacia los hosts C, D y E.

## Conmutación de circuitos (*circuit switching*)

En vez de enviar paquetes sueltos, primero se **establece una conexión** entre origen y destino, eligiendo un camino y reservando recursos en cada tramo. Es el enfoque de la **comunicación telefónica**: al llamar, la conexión no es instantánea, porque primero se arma el circuito.

- **Ancho de banda garantizado** durante toda la comunicación.
- **Sensible a la saturación** ante muchas conexiones simultáneas: por ejemplo, tras un terremoto las líneas colapsan porque todos llaman a la vez.
- Un enlace de 1 Mbps con 4 conexiones simultáneas le da a cada una hasta **250 kbps**, la use o no.

Para mantener separadas las comunicaciones en un medio compartido se usa **multiplexación**:

- **FDM** (*Frequency-Division Multiplexing*): cada transmisión tiene su banda de frecuencia.
- **TDM** (*Time-Division Multiplexing*): cada emisor tiene un turno para transmitir con todo el ancho de banda.

![Conmutación de circuitos circuit switching y reserva de recursos](adjuntos/Conmutaci%C3%B3n%20de%20circuitos%20circuit%20switching%20y%20reserva%20de%20recursos.png)

> [!example]- Transcripción de la imagen
> "CIRCUIT SWITCHING. Establecimiento previo de conexión entre origen-destino. *Ancho de banda garantizado durante comunicación*. Enfoque usado por comunicación **telefónica**. Sensible a saturación ante conexiones simultáneas. Enlace de 1Mbps, con 4 conexiones simultáneas, cada una recibe hasta 250kbps. Si hay N enlaces iguales en la ruta, el tiempo de transmisión de origen a destino (*end-to-end delay*) es: $d_{end-to-end} = N \times \frac{L}{R}$". A la derecha, cuatro switches en cuadrado con un camino resaltado en azul entre dos computadores.

| | Paquetes | Circuitos |
|---|---|---|
| Antes de transmitir | Nada: se envía de inmediato | Hay que establecer el circuito |
| Recursos | Compartidos según demanda | Reservados, aunque no se usen |
| Ante congestión | Colas y posible pérdida de paquetes | Rechazo de nuevas conexiones |
| Uso | Internet | Telefonía tradicional |

## Preguntas de repaso

> [!question]- ¿Cuánto demora transmitir 1500 bytes por un enlace de 100 Mbps?
> $L = 12\,000$ bits, así que $d = 12\,000 / 10^8 = 120\ \mu s$.

> [!question]- ¿Por qué con conmutación de paquetes el retardo de extremo a extremo es $N \times L/R$?
> Porque cada router almacena el paquete completo antes de reenviarlo (*store-and-forward*): en cada uno de los $N$ enlaces se paga de nuevo la transmisión $L/R$.

> [!question]- ¿Qué pasa en un router congestionado?
> Los paquetes que no alcanzan a salir esperan en una cola de memoria limitada; si la cola se llena, los nuevos paquetes se pierden.

> [!question]- ¿Qué ventaja y qué desventaja tiene la conmutación de circuitos?
> Garantiza un ancho de banda durante toda la comunicación. Pero exige establecer el circuito antes, reserva recursos aunque no se usen y se satura cuando hay muchas conexiones simultáneas.
